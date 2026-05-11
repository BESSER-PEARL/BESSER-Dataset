import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Value,
    imp::BoolValue,
    imp::IntValue,
    Expr,
    imp::Binary,
    imp::Unary,
    imp::Var,
    imp::IntConst,
    imp::Value,
    imp::StringToValueMap,
    imp::Store,
    imp::Stmt,
    imp::Expr,
    Stmt,
    imp::While,
    imp::Assign,
    imp::Block,
    imp::If,
    imp::Skip,
    UnaryOp,
    BinaryOp,
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



def test_imp::boolvalue_is_not_abstract():
    assert not inspect.isabstract(imp::BoolValue)


def test_imp::boolvalue_constructor_exists():
    assert callable(imp::BoolValue.__init__)


def test_imp::boolvalue_constructor_args():
    sig = inspect.signature(imp::BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::boolvalue_has_value():
    assert hasattr(imp::BoolValue, "value")
    descriptor = None
    for klass in imp::BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::intvalue_is_not_abstract():
    assert not inspect.isabstract(imp::IntValue)


def test_imp::intvalue_constructor_exists():
    assert callable(imp::IntValue.__init__)


def test_imp::intvalue_constructor_args():
    sig = inspect.signature(imp::IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::intvalue_has_value():
    assert hasattr(imp::IntValue, "value")
    descriptor = None
    for klass in imp::IntValue.__mro__:
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



def test_imp::binary_is_not_abstract():
    assert not inspect.isabstract(imp::Binary)


def test_imp::binary_constructor_exists():
    assert callable(imp::Binary.__init__)


def test_imp::binary_constructor_args():
    sig = inspect.signature(imp::Binary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp::binary_has_op():
    assert hasattr(imp::Binary, "op")
    descriptor = None
    for klass in imp::Binary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp::unary_is_not_abstract():
    assert not inspect.isabstract(imp::Unary)


def test_imp::unary_constructor_exists():
    assert callable(imp::Unary.__init__)


def test_imp::unary_constructor_args():
    sig = inspect.signature(imp::Unary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp::unary_has_op():
    assert hasattr(imp::Unary, "op")
    descriptor = None
    for klass in imp::Unary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp::var_is_not_abstract():
    assert not inspect.isabstract(imp::Var)


def test_imp::var_constructor_exists():
    assert callable(imp::Var.__init__)


def test_imp::var_constructor_args():
    sig = inspect.signature(imp::Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::var_has_name():
    assert hasattr(imp::Var, "name")
    descriptor = None
    for klass in imp::Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp::intconst_is_not_abstract():
    assert not inspect.isabstract(imp::IntConst)


def test_imp::intconst_constructor_exists():
    assert callable(imp::IntConst.__init__)


def test_imp::intconst_constructor_args():
    sig = inspect.signature(imp::IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::intconst_has_value():
    assert hasattr(imp::IntConst, "value")
    descriptor = None
    for klass in imp::IntConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::value_is_not_abstract():
    assert not inspect.isabstract(imp::Value)


def test_imp::value_constructor_exists():
    assert callable(imp::Value.__init__)


def test_imp::value_constructor_args():
    sig = inspect.signature(imp::Value.__init__)
    params = list(sig.parameters.keys())



def test_imp::stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(imp::StringToValueMap)


def test_imp::stringtovaluemap_constructor_exists():
    assert callable(imp::StringToValueMap.__init__)


def test_imp::stringtovaluemap_constructor_args():
    sig = inspect.signature(imp::StringToValueMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_imp::stringtovaluemap_has_key():
    assert hasattr(imp::StringToValueMap, "key")
    descriptor = None
    for klass in imp::StringToValueMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_imp::store_is_not_abstract():
    assert not inspect.isabstract(imp::Store)


def test_imp::store_constructor_exists():
    assert callable(imp::Store.__init__)


def test_imp::store_constructor_args():
    sig = inspect.signature(imp::Store.__init__)
    params = list(sig.parameters.keys())



def test_imp::stmt_is_not_abstract():
    assert not inspect.isabstract(imp::Stmt)


def test_imp::stmt_constructor_exists():
    assert callable(imp::Stmt.__init__)


def test_imp::stmt_constructor_args():
    sig = inspect.signature(imp::Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp::expr_is_not_abstract():
    assert not inspect.isabstract(imp::Expr)


def test_imp::expr_constructor_exists():
    assert callable(imp::Expr.__init__)


def test_imp::expr_constructor_args():
    sig = inspect.signature(imp::Expr.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp::while_is_not_abstract():
    assert not inspect.isabstract(imp::While)


def test_imp::while_constructor_exists():
    assert callable(imp::While.__init__)


def test_imp::while_constructor_args():
    sig = inspect.signature(imp::While.__init__)
    params = list(sig.parameters.keys())



def test_imp::assign_is_not_abstract():
    assert not inspect.isabstract(imp::Assign)


def test_imp::assign_constructor_exists():
    assert callable(imp::Assign.__init__)


def test_imp::assign_constructor_args():
    sig = inspect.signature(imp::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::assign_has_name():
    assert hasattr(imp::Assign, "name")
    descriptor = None
    for klass in imp::Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp::block_is_not_abstract():
    assert not inspect.isabstract(imp::Block)


def test_imp::block_constructor_exists():
    assert callable(imp::Block.__init__)


def test_imp::block_constructor_args():
    sig = inspect.signature(imp::Block.__init__)
    params = list(sig.parameters.keys())



def test_imp::if_is_not_abstract():
    assert not inspect.isabstract(imp::If)


def test_imp::if_constructor_exists():
    assert callable(imp::If.__init__)


def test_imp::if_constructor_args():
    sig = inspect.signature(imp::If.__init__)
    params = list(sig.parameters.keys())



def test_imp::skip_is_not_abstract():
    assert not inspect.isabstract(imp::Skip)


def test_imp::skip_constructor_exists():
    assert callable(imp::Skip.__init__)


def test_imp::skip_constructor_args():
    sig = inspect.signature(imp::Skip.__init__)
    params = list(sig.parameters.keys())

def test_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "NOT",
        "NEGATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "OR",
        "EQ",
        "AND",
        "LT",
        "GEQ",
        "SUB",
        "LEQ",
        "GT",
        "MUL",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"


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
imp::BoolValue_strategy = st.builds(
    imp::BoolValue,
    value=
        st.booleans()
)
imp::IntValue_strategy = st.builds(
    imp::IntValue,
    value=
        st.integers()
)
Expr_strategy = st.builds(
    Expr,
)
imp::Binary_strategy = st.builds(
    imp::Binary,
    op=
        safe_text
)
imp::Unary_strategy = st.builds(
    imp::Unary,
    op=
        safe_text
)
imp::Var_strategy = st.builds(
    imp::Var,
    name=
        safe_text
)
imp::IntConst_strategy = st.builds(
    imp::IntConst,
    value=
        st.integers()
)
imp::Value_strategy = st.builds(
    imp::Value,
)
imp::StringToValueMap_strategy = st.builds(
    imp::StringToValueMap,
    key=
        safe_text
)
imp::Store_strategy = st.builds(
    imp::Store,
)
imp::Stmt_strategy = st.builds(
    imp::Stmt,
)
imp::Expr_strategy = st.builds(
    imp::Expr,
)
Stmt_strategy = st.builds(
    Stmt,
)
imp::While_strategy = st.builds(
    imp::While,
)
imp::Assign_strategy = st.builds(
    imp::Assign,
    name=
        safe_text
)
imp::Block_strategy = st.builds(
    imp::Block,
)
imp::If_strategy = st.builds(
    imp::If,
)
imp::Skip_strategy = st.builds(
    imp::Skip,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=imp::BoolValue_strategy)
@settings(max_examples=50)
def test_imp::boolvalue_instantiation(instance):
    assert isinstance(instance, imp::BoolValue)

@given(instance=imp::BoolValue_strategy)
def test_imp::boolvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=imp::BoolValue_strategy)
def test_imp::boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::IntValue_strategy)
@settings(max_examples=50)
def test_imp::intvalue_instantiation(instance):
    assert isinstance(instance, imp::IntValue)

@given(instance=imp::IntValue_strategy)
def test_imp::intvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=imp::IntValue_strategy)
def test_imp::intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=imp::Binary_strategy)
@settings(max_examples=50)
def test_imp::binary_instantiation(instance):
    assert isinstance(instance, imp::Binary)

@given(instance=imp::Binary_strategy)
def test_imp::binary_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=imp::Binary_strategy)
def test_imp::binary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp::Unary_strategy)
@settings(max_examples=50)
def test_imp::unary_instantiation(instance):
    assert isinstance(instance, imp::Unary)

@given(instance=imp::Unary_strategy)
def test_imp::unary_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=imp::Unary_strategy)
def test_imp::unary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp::Var_strategy)
@settings(max_examples=50)
def test_imp::var_instantiation(instance):
    assert isinstance(instance, imp::Var)

@given(instance=imp::Var_strategy)
def test_imp::var_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::Var_strategy)
def test_imp::var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp::IntConst_strategy)
@settings(max_examples=50)
def test_imp::intconst_instantiation(instance):
    assert isinstance(instance, imp::IntConst)

@given(instance=imp::IntConst_strategy)
def test_imp::intconst_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=imp::IntConst_strategy)
def test_imp::intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::Value_strategy)
@settings(max_examples=50)
def test_imp::value_instantiation(instance):
    assert isinstance(instance, imp::Value)

@given(instance=imp::StringToValueMap_strategy)
@settings(max_examples=50)
def test_imp::stringtovaluemap_instantiation(instance):
    assert isinstance(instance, imp::StringToValueMap)

@given(instance=imp::StringToValueMap_strategy)
def test_imp::stringtovaluemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=imp::StringToValueMap_strategy)
def test_imp::stringtovaluemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=imp::Store_strategy)
@settings(max_examples=50)
def test_imp::store_instantiation(instance):
    assert isinstance(instance, imp::Store)

@given(instance=imp::Stmt_strategy)
@settings(max_examples=50)
def test_imp::stmt_instantiation(instance):
    assert isinstance(instance, imp::Stmt)

@given(instance=imp::Expr_strategy)
@settings(max_examples=50)
def test_imp::expr_instantiation(instance):
    assert isinstance(instance, imp::Expr)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=imp::While_strategy)
@settings(max_examples=50)
def test_imp::while_instantiation(instance):
    assert isinstance(instance, imp::While)

@given(instance=imp::Assign_strategy)
@settings(max_examples=50)
def test_imp::assign_instantiation(instance):
    assert isinstance(instance, imp::Assign)

@given(instance=imp::Assign_strategy)
def test_imp::assign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::Assign_strategy)
def test_imp::assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp::Block_strategy)
@settings(max_examples=50)
def test_imp::block_instantiation(instance):
    assert isinstance(instance, imp::Block)

@given(instance=imp::If_strategy)
@settings(max_examples=50)
def test_imp::if_instantiation(instance):
    assert isinstance(instance, imp::If)

@given(instance=imp::Skip_strategy)
@settings(max_examples=50)
def test_imp::skip_instantiation(instance):
    assert isinstance(instance, imp::Skip)
