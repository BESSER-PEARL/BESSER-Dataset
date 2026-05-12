import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    imp_BoolValue,
    imp_IntValue,
    Expr,
    imp_Binary,
    imp_Unary,
    imp_Var,
    imp_IntConst,
    imp_Value,
    imp_StringToValueMap,
    imp_Store,
    imp_Stmt,
    imp_Expr,
    Stmt,
    imp_If,
    imp_Block,
    imp_Assign,
    imp_While,
    imp_Skip,
    BinaryOp,
    UnaryOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_imp_boolvalue_is_not_abstract():
    assert not inspect.isabstract(imp_BoolValue)


def test_imp_boolvalue_constructor_exists():
    assert callable(imp_BoolValue.__init__)


def test_imp_boolvalue_constructor_args():
    sig = inspect.signature(imp_BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_boolvalue_has_value():
    assert hasattr(imp_BoolValue, "value")
    descriptor = None
    for klass in imp_BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_intvalue_is_not_abstract():
    assert not inspect.isabstract(imp_IntValue)


def test_imp_intvalue_constructor_exists():
    assert callable(imp_IntValue.__init__)


def test_imp_intvalue_constructor_args():
    sig = inspect.signature(imp_IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_intvalue_has_value():
    assert hasattr(imp_IntValue, "value")
    descriptor = None
    for klass in imp_IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_imp_binary_is_not_abstract():
    assert not inspect.isabstract(imp_Binary)


def test_imp_binary_constructor_exists():
    assert callable(imp_Binary.__init__)


def test_imp_binary_constructor_args():
    sig = inspect.signature(imp_Binary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp_binary_has_op():
    assert hasattr(imp_Binary, "op")
    descriptor = None
    for klass in imp_Binary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp_unary_is_not_abstract():
    assert not inspect.isabstract(imp_Unary)


def test_imp_unary_constructor_exists():
    assert callable(imp_Unary.__init__)


def test_imp_unary_constructor_args():
    sig = inspect.signature(imp_Unary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp_unary_has_op():
    assert hasattr(imp_Unary, "op")
    descriptor = None
    for klass in imp_Unary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp_var_is_not_abstract():
    assert not inspect.isabstract(imp_Var)


def test_imp_var_constructor_exists():
    assert callable(imp_Var.__init__)


def test_imp_var_constructor_args():
    sig = inspect.signature(imp_Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_var_has_name():
    assert hasattr(imp_Var, "name")
    descriptor = None
    for klass in imp_Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp_intconst_is_not_abstract():
    assert not inspect.isabstract(imp_IntConst)


def test_imp_intconst_constructor_exists():
    assert callable(imp_IntConst.__init__)


def test_imp_intconst_constructor_args():
    sig = inspect.signature(imp_IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_intconst_has_value():
    assert hasattr(imp_IntConst, "value")
    descriptor = None
    for klass in imp_IntConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_value_is_not_abstract():
    assert not inspect.isabstract(imp_Value)


def test_imp_value_constructor_exists():
    assert callable(imp_Value.__init__)


def test_imp_value_constructor_args():
    sig = inspect.signature(imp_Value.__init__)
    params = list(sig.parameters.keys())



def test_imp_stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(imp_StringToValueMap)


def test_imp_stringtovaluemap_constructor_exists():
    assert callable(imp_StringToValueMap.__init__)


def test_imp_stringtovaluemap_constructor_args():
    sig = inspect.signature(imp_StringToValueMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_imp_stringtovaluemap_has_key():
    assert hasattr(imp_StringToValueMap, "key")
    descriptor = None
    for klass in imp_StringToValueMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_imp_store_is_not_abstract():
    assert not inspect.isabstract(imp_Store)


def test_imp_store_constructor_exists():
    assert callable(imp_Store.__init__)


def test_imp_store_constructor_args():
    sig = inspect.signature(imp_Store.__init__)
    params = list(sig.parameters.keys())



def test_imp_stmt_is_not_abstract():
    assert not inspect.isabstract(imp_Stmt)


def test_imp_stmt_constructor_exists():
    assert callable(imp_Stmt.__init__)


def test_imp_stmt_constructor_args():
    sig = inspect.signature(imp_Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp_expr_is_not_abstract():
    assert not inspect.isabstract(imp_Expr)


def test_imp_expr_constructor_exists():
    assert callable(imp_Expr.__init__)


def test_imp_expr_constructor_args():
    sig = inspect.signature(imp_Expr.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp_if_is_not_abstract():
    assert not inspect.isabstract(imp_If)


def test_imp_if_constructor_exists():
    assert callable(imp_If.__init__)


def test_imp_if_constructor_args():
    sig = inspect.signature(imp_If.__init__)
    params = list(sig.parameters.keys())



def test_imp_block_is_not_abstract():
    assert not inspect.isabstract(imp_Block)


def test_imp_block_constructor_exists():
    assert callable(imp_Block.__init__)


def test_imp_block_constructor_args():
    sig = inspect.signature(imp_Block.__init__)
    params = list(sig.parameters.keys())



def test_imp_assign_is_not_abstract():
    assert not inspect.isabstract(imp_Assign)


def test_imp_assign_constructor_exists():
    assert callable(imp_Assign.__init__)


def test_imp_assign_constructor_args():
    sig = inspect.signature(imp_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_assign_has_name():
    assert hasattr(imp_Assign, "name")
    descriptor = None
    for klass in imp_Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp_while_is_not_abstract():
    assert not inspect.isabstract(imp_While)


def test_imp_while_constructor_exists():
    assert callable(imp_While.__init__)


def test_imp_while_constructor_args():
    sig = inspect.signature(imp_While.__init__)
    params = list(sig.parameters.keys())



def test_imp_skip_is_not_abstract():
    assert not inspect.isabstract(imp_Skip)


def test_imp_skip_constructor_exists():
    assert callable(imp_Skip.__init__)


def test_imp_skip_constructor_args():
    sig = inspect.signature(imp_Skip.__init__)
    params = list(sig.parameters.keys())

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "ADD",
        "MUL",
        "GT",
        "OR",
        "LEQ",
        "EQ",
        "LT",
        "GEQ",
        "SUB",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"

def test_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "NEGATE",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"


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
Value_strategy = st.builds(
    Value,
)
imp_BoolValue_strategy = st.builds(
    imp_BoolValue,
    value=
        st.booleans()
)
imp_IntValue_strategy = st.builds(
    imp_IntValue,
    value=
        st.integers()
)
Expr_strategy = st.builds(
    Expr,
)
imp_Binary_strategy = st.builds(
    imp_Binary,
    op=
        safe_text
)
imp_Unary_strategy = st.builds(
    imp_Unary,
    op=
        safe_text
)
imp_Var_strategy = st.builds(
    imp_Var,
    name=
        safe_text
)
imp_IntConst_strategy = st.builds(
    imp_IntConst,
    value=
        st.integers()
)
imp_Value_strategy = st.builds(
    imp_Value,
)
imp_StringToValueMap_strategy = st.builds(
    imp_StringToValueMap,
    key=
        safe_text
)
imp_Store_strategy = st.builds(
    imp_Store,
)
imp_Stmt_strategy = st.builds(
    imp_Stmt,
)
imp_Expr_strategy = st.builds(
    imp_Expr,
)
Stmt_strategy = st.builds(
    Stmt,
)
imp_If_strategy = st.builds(
    imp_If,
)
imp_Block_strategy = st.builds(
    imp_Block,
)
imp_Assign_strategy = st.builds(
    imp_Assign,
    name=
        safe_text
)
imp_While_strategy = st.builds(
    imp_While,
)
imp_Skip_strategy = st.builds(
    imp_Skip,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=imp_BoolValue_strategy)
@settings(max_examples=50)
def test_imp_boolvalue_instantiation(instance):
    assert isinstance(instance, imp_BoolValue)



@given(instance=imp_BoolValue_strategy)
def test_imp_boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_IntValue_strategy)
@settings(max_examples=50)
def test_imp_intvalue_instantiation(instance):
    assert isinstance(instance, imp_IntValue)



@given(instance=imp_IntValue_strategy)
def test_imp_intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=imp_Binary_strategy)
@settings(max_examples=50)
def test_imp_binary_instantiation(instance):
    assert isinstance(instance, imp_Binary)



@given(instance=imp_Binary_strategy)
def test_imp_binary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp_Unary_strategy)
@settings(max_examples=50)
def test_imp_unary_instantiation(instance):
    assert isinstance(instance, imp_Unary)



@given(instance=imp_Unary_strategy)
def test_imp_unary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp_Var_strategy)
@settings(max_examples=50)
def test_imp_var_instantiation(instance):
    assert isinstance(instance, imp_Var)



@given(instance=imp_Var_strategy)
def test_imp_var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp_IntConst_strategy)
@settings(max_examples=50)
def test_imp_intconst_instantiation(instance):
    assert isinstance(instance, imp_IntConst)



@given(instance=imp_IntConst_strategy)
def test_imp_intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_Value_strategy)
@settings(max_examples=50)
def test_imp_value_instantiation(instance):
    assert isinstance(instance, imp_Value)

@given(instance=imp_StringToValueMap_strategy)
@settings(max_examples=50)
def test_imp_stringtovaluemap_instantiation(instance):
    assert isinstance(instance, imp_StringToValueMap)



@given(instance=imp_StringToValueMap_strategy)
def test_imp_stringtovaluemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=imp_Store_strategy)
@settings(max_examples=50)
def test_imp_store_instantiation(instance):
    assert isinstance(instance, imp_Store)

@given(instance=imp_Stmt_strategy)
@settings(max_examples=50)
def test_imp_stmt_instantiation(instance):
    assert isinstance(instance, imp_Stmt)

@given(instance=imp_Expr_strategy)
@settings(max_examples=50)
def test_imp_expr_instantiation(instance):
    assert isinstance(instance, imp_Expr)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=imp_If_strategy)
@settings(max_examples=50)
def test_imp_if_instantiation(instance):
    assert isinstance(instance, imp_If)

@given(instance=imp_Block_strategy)
@settings(max_examples=50)
def test_imp_block_instantiation(instance):
    assert isinstance(instance, imp_Block)

@given(instance=imp_Assign_strategy)
@settings(max_examples=50)
def test_imp_assign_instantiation(instance):
    assert isinstance(instance, imp_Assign)



@given(instance=imp_Assign_strategy)
def test_imp_assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp_While_strategy)
@settings(max_examples=50)
def test_imp_while_instantiation(instance):
    assert isinstance(instance, imp_While)

@given(instance=imp_Skip_strategy)
@settings(max_examples=50)
def test_imp_skip_instantiation(instance):
    assert isinstance(instance, imp_Skip)
