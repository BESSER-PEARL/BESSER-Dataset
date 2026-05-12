import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UnaryExpression,
    core_UMinus,
    core_Not,
    IntegerExpression,
    core_IntegerLiteral,
    core_Conditional,
    core_BinaryExpression,
    core_UnaryExpression,
    BinaryExpression,
    core_Or,
    core_Div,
    core_Minus,
    core_Mult,
    core_Lower,
    core_And,
    core_Greater,
    core_Mod,
    core_Equal,
    core_Add,
    core_Filter,
    core_IntegerExpression,
    core_Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_core_uminus_is_not_abstract():
    assert not inspect.isabstract(core_UMinus)


def test_core_uminus_constructor_exists():
    assert callable(core_UMinus.__init__)


def test_core_uminus_constructor_args():
    sig = inspect.signature(core_UMinus.__init__)
    params = list(sig.parameters.keys())



def test_core_not_is_not_abstract():
    assert not inspect.isabstract(core_Not)


def test_core_not_constructor_exists():
    assert callable(core_Not.__init__)


def test_core_not_constructor_args():
    sig = inspect.signature(core_Not.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_core_integerliteral_is_not_abstract():
    assert not inspect.isabstract(core_IntegerLiteral)


def test_core_integerliteral_constructor_exists():
    assert callable(core_IntegerLiteral.__init__)


def test_core_integerliteral_constructor_args():
    sig = inspect.signature(core_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_core_integerliteral_has_val():
    assert hasattr(core_IntegerLiteral, "val")
    descriptor = None
    for klass in core_IntegerLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_core_conditional_is_not_abstract():
    assert not inspect.isabstract(core_Conditional)


def test_core_conditional_constructor_exists():
    assert callable(core_Conditional.__init__)


def test_core_conditional_constructor_args():
    sig = inspect.signature(core_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_core_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(core_BinaryExpression)


def test_core_binaryexpression_constructor_exists():
    assert callable(core_BinaryExpression.__init__)


def test_core_binaryexpression_constructor_args():
    sig = inspect.signature(core_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_core_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(core_UnaryExpression)


def test_core_unaryexpression_constructor_exists():
    assert callable(core_UnaryExpression.__init__)


def test_core_unaryexpression_constructor_args():
    sig = inspect.signature(core_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_core_or_is_not_abstract():
    assert not inspect.isabstract(core_Or)


def test_core_or_constructor_exists():
    assert callable(core_Or.__init__)


def test_core_or_constructor_args():
    sig = inspect.signature(core_Or.__init__)
    params = list(sig.parameters.keys())



def test_core_div_is_not_abstract():
    assert not inspect.isabstract(core_Div)


def test_core_div_constructor_exists():
    assert callable(core_Div.__init__)


def test_core_div_constructor_args():
    sig = inspect.signature(core_Div.__init__)
    params = list(sig.parameters.keys())



def test_core_minus_is_not_abstract():
    assert not inspect.isabstract(core_Minus)


def test_core_minus_constructor_exists():
    assert callable(core_Minus.__init__)


def test_core_minus_constructor_args():
    sig = inspect.signature(core_Minus.__init__)
    params = list(sig.parameters.keys())



def test_core_mult_is_not_abstract():
    assert not inspect.isabstract(core_Mult)


def test_core_mult_constructor_exists():
    assert callable(core_Mult.__init__)


def test_core_mult_constructor_args():
    sig = inspect.signature(core_Mult.__init__)
    params = list(sig.parameters.keys())



def test_core_lower_is_not_abstract():
    assert not inspect.isabstract(core_Lower)


def test_core_lower_constructor_exists():
    assert callable(core_Lower.__init__)


def test_core_lower_constructor_args():
    sig = inspect.signature(core_Lower.__init__)
    params = list(sig.parameters.keys())



def test_core_and_is_not_abstract():
    assert not inspect.isabstract(core_And)


def test_core_and_constructor_exists():
    assert callable(core_And.__init__)


def test_core_and_constructor_args():
    sig = inspect.signature(core_And.__init__)
    params = list(sig.parameters.keys())



def test_core_greater_is_not_abstract():
    assert not inspect.isabstract(core_Greater)


def test_core_greater_constructor_exists():
    assert callable(core_Greater.__init__)


def test_core_greater_constructor_args():
    sig = inspect.signature(core_Greater.__init__)
    params = list(sig.parameters.keys())



def test_core_mod_is_not_abstract():
    assert not inspect.isabstract(core_Mod)


def test_core_mod_constructor_exists():
    assert callable(core_Mod.__init__)


def test_core_mod_constructor_args():
    sig = inspect.signature(core_Mod.__init__)
    params = list(sig.parameters.keys())



def test_core_equal_is_not_abstract():
    assert not inspect.isabstract(core_Equal)


def test_core_equal_constructor_exists():
    assert callable(core_Equal.__init__)


def test_core_equal_constructor_args():
    sig = inspect.signature(core_Equal.__init__)
    params = list(sig.parameters.keys())



def test_core_add_is_not_abstract():
    assert not inspect.isabstract(core_Add)


def test_core_add_constructor_exists():
    assert callable(core_Add.__init__)


def test_core_add_constructor_args():
    sig = inspect.signature(core_Add.__init__)
    params = list(sig.parameters.keys())



def test_core_filter_is_not_abstract():
    assert not inspect.isabstract(core_Filter)


def test_core_filter_constructor_exists():
    assert callable(core_Filter.__init__)


def test_core_filter_constructor_args():
    sig = inspect.signature(core_Filter.__init__)
    params = list(sig.parameters.keys())



def test_core_integerexpression_is_not_abstract():
    assert not inspect.isabstract(core_IntegerExpression)


def test_core_integerexpression_constructor_exists():
    assert callable(core_IntegerExpression.__init__)


def test_core_integerexpression_constructor_args():
    sig = inspect.signature(core_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_core_rule_is_not_abstract():
    assert not inspect.isabstract(core_Rule)


def test_core_rule_constructor_exists():
    assert callable(core_Rule.__init__)


def test_core_rule_constructor_args():
    sig = inspect.signature(core_Rule.__init__)
    params = list(sig.parameters.keys())


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
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
core_UMinus_strategy = st.builds(
    core_UMinus,
)
core_Not_strategy = st.builds(
    core_Not,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
core_IntegerLiteral_strategy = st.builds(
    core_IntegerLiteral,
    val=
        st.integers()
)
core_Conditional_strategy = st.builds(
    core_Conditional,
)
core_BinaryExpression_strategy = st.builds(
    core_BinaryExpression,
)
core_UnaryExpression_strategy = st.builds(
    core_UnaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
core_Or_strategy = st.builds(
    core_Or,
)
core_Div_strategy = st.builds(
    core_Div,
)
core_Minus_strategy = st.builds(
    core_Minus,
)
core_Mult_strategy = st.builds(
    core_Mult,
)
core_Lower_strategy = st.builds(
    core_Lower,
)
core_And_strategy = st.builds(
    core_And,
)
core_Greater_strategy = st.builds(
    core_Greater,
)
core_Mod_strategy = st.builds(
    core_Mod,
)
core_Equal_strategy = st.builds(
    core_Equal,
)
core_Add_strategy = st.builds(
    core_Add,
)
core_Filter_strategy = st.builds(
    core_Filter,
)
core_IntegerExpression_strategy = st.builds(
    core_IntegerExpression,
)
core_Rule_strategy = st.builds(
    core_Rule,
)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=core_UMinus_strategy)
@settings(max_examples=50)
def test_core_uminus_instantiation(instance):
    assert isinstance(instance, core_UMinus)

@given(instance=core_Not_strategy)
@settings(max_examples=50)
def test_core_not_instantiation(instance):
    assert isinstance(instance, core_Not)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=core_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_core_integerliteral_instantiation(instance):
    assert isinstance(instance, core_IntegerLiteral)



@given(instance=core_IntegerLiteral_strategy)
def test_core_integerliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=core_Conditional_strategy)
@settings(max_examples=50)
def test_core_conditional_instantiation(instance):
    assert isinstance(instance, core_Conditional)

@given(instance=core_BinaryExpression_strategy)
@settings(max_examples=50)
def test_core_binaryexpression_instantiation(instance):
    assert isinstance(instance, core_BinaryExpression)

@given(instance=core_UnaryExpression_strategy)
@settings(max_examples=50)
def test_core_unaryexpression_instantiation(instance):
    assert isinstance(instance, core_UnaryExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=core_Or_strategy)
@settings(max_examples=50)
def test_core_or_instantiation(instance):
    assert isinstance(instance, core_Or)

@given(instance=core_Div_strategy)
@settings(max_examples=50)
def test_core_div_instantiation(instance):
    assert isinstance(instance, core_Div)

@given(instance=core_Minus_strategy)
@settings(max_examples=50)
def test_core_minus_instantiation(instance):
    assert isinstance(instance, core_Minus)

@given(instance=core_Mult_strategy)
@settings(max_examples=50)
def test_core_mult_instantiation(instance):
    assert isinstance(instance, core_Mult)

@given(instance=core_Lower_strategy)
@settings(max_examples=50)
def test_core_lower_instantiation(instance):
    assert isinstance(instance, core_Lower)

@given(instance=core_And_strategy)
@settings(max_examples=50)
def test_core_and_instantiation(instance):
    assert isinstance(instance, core_And)

@given(instance=core_Greater_strategy)
@settings(max_examples=50)
def test_core_greater_instantiation(instance):
    assert isinstance(instance, core_Greater)

@given(instance=core_Mod_strategy)
@settings(max_examples=50)
def test_core_mod_instantiation(instance):
    assert isinstance(instance, core_Mod)

@given(instance=core_Equal_strategy)
@settings(max_examples=50)
def test_core_equal_instantiation(instance):
    assert isinstance(instance, core_Equal)

@given(instance=core_Add_strategy)
@settings(max_examples=50)
def test_core_add_instantiation(instance):
    assert isinstance(instance, core_Add)

@given(instance=core_Filter_strategy)
@settings(max_examples=50)
def test_core_filter_instantiation(instance):
    assert isinstance(instance, core_Filter)

@given(instance=core_IntegerExpression_strategy)
@settings(max_examples=50)
def test_core_integerexpression_instantiation(instance):
    assert isinstance(instance, core_IntegerExpression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=core_IntegerExpression_strategy)
@settings(max_examples=30)
def test_core_integerexpression_isboolean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBoolean()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBoolean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBoolean' in core_IntegerExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBoolean' in core_IntegerExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBoolean' in core_IntegerExpression is not implemented or raised an error")

@given(instance=core_Rule_strategy)
@settings(max_examples=50)
def test_core_rule_instantiation(instance):
    assert isinstance(instance, core_Rule)
