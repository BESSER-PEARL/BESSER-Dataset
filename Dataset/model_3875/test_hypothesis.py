import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinaryExp,
    fl_MinusExp,
    fl_EqualExp,
    fl_PlusExp,
    Exp,
    fl_IfThenElseExp,
    fl_ArgumentExp,
    fl_ApplyExp,
    fl_LiteralExp,
    fl_Exp,
    fl_Argument,
    fl_Function,
    fl_Program,
    fl_BinaryExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_fl_minusexp_is_not_abstract():
    assert not inspect.isabstract(fl_MinusExp)


def test_fl_minusexp_constructor_exists():
    assert callable(fl_MinusExp.__init__)


def test_fl_minusexp_constructor_args():
    sig = inspect.signature(fl_MinusExp.__init__)
    params = list(sig.parameters.keys())



def test_fl_equalexp_is_not_abstract():
    assert not inspect.isabstract(fl_EqualExp)


def test_fl_equalexp_constructor_exists():
    assert callable(fl_EqualExp.__init__)


def test_fl_equalexp_constructor_args():
    sig = inspect.signature(fl_EqualExp.__init__)
    params = list(sig.parameters.keys())



def test_fl_plusexp_is_not_abstract():
    assert not inspect.isabstract(fl_PlusExp)


def test_fl_plusexp_constructor_exists():
    assert callable(fl_PlusExp.__init__)


def test_fl_plusexp_constructor_args():
    sig = inspect.signature(fl_PlusExp.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_fl_ifthenelseexp_is_not_abstract():
    assert not inspect.isabstract(fl_IfThenElseExp)


def test_fl_ifthenelseexp_constructor_exists():
    assert callable(fl_IfThenElseExp.__init__)


def test_fl_ifthenelseexp_constructor_args():
    sig = inspect.signature(fl_IfThenElseExp.__init__)
    params = list(sig.parameters.keys())



def test_fl_argumentexp_is_not_abstract():
    assert not inspect.isabstract(fl_ArgumentExp)


def test_fl_argumentexp_constructor_exists():
    assert callable(fl_ArgumentExp.__init__)


def test_fl_argumentexp_constructor_args():
    sig = inspect.signature(fl_ArgumentExp.__init__)
    params = list(sig.parameters.keys())



def test_fl_applyexp_is_not_abstract():
    assert not inspect.isabstract(fl_ApplyExp)


def test_fl_applyexp_constructor_exists():
    assert callable(fl_ApplyExp.__init__)


def test_fl_applyexp_constructor_args():
    sig = inspect.signature(fl_ApplyExp.__init__)
    params = list(sig.parameters.keys())



def test_fl_literalexp_is_not_abstract():
    assert not inspect.isabstract(fl_LiteralExp)


def test_fl_literalexp_constructor_exists():
    assert callable(fl_LiteralExp.__init__)


def test_fl_literalexp_constructor_args():
    sig = inspect.signature(fl_LiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fl_literalexp_has_value():
    assert hasattr(fl_LiteralExp, "value")
    descriptor = None
    for klass in fl_LiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fl_exp_is_not_abstract():
    assert not inspect.isabstract(fl_Exp)


def test_fl_exp_constructor_exists():
    assert callable(fl_Exp.__init__)


def test_fl_exp_constructor_args():
    sig = inspect.signature(fl_Exp.__init__)
    params = list(sig.parameters.keys())



def test_fl_argument_is_not_abstract():
    assert not inspect.isabstract(fl_Argument)


def test_fl_argument_constructor_exists():
    assert callable(fl_Argument.__init__)


def test_fl_argument_constructor_args():
    sig = inspect.signature(fl_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl_argument_has_name():
    assert hasattr(fl_Argument, "name")
    descriptor = None
    for klass in fl_Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl_function_is_not_abstract():
    assert not inspect.isabstract(fl_Function)


def test_fl_function_constructor_exists():
    assert callable(fl_Function.__init__)


def test_fl_function_constructor_args():
    sig = inspect.signature(fl_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl_function_has_name():
    assert hasattr(fl_Function, "name")
    descriptor = None
    for klass in fl_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl_program_is_not_abstract():
    assert not inspect.isabstract(fl_Program)


def test_fl_program_constructor_exists():
    assert callable(fl_Program.__init__)


def test_fl_program_constructor_args():
    sig = inspect.signature(fl_Program.__init__)
    params = list(sig.parameters.keys())



def test_fl_binaryexp_is_not_abstract():
    assert not inspect.isabstract(fl_BinaryExp)


def test_fl_binaryexp_constructor_exists():
    assert callable(fl_BinaryExp.__init__)


def test_fl_binaryexp_constructor_args():
    sig = inspect.signature(fl_BinaryExp.__init__)
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
BinaryExp_strategy = st.builds(
    BinaryExp,
)
fl_MinusExp_strategy = st.builds(
    fl_MinusExp,
)
fl_EqualExp_strategy = st.builds(
    fl_EqualExp,
)
fl_PlusExp_strategy = st.builds(
    fl_PlusExp,
)
Exp_strategy = st.builds(
    Exp,
)
fl_IfThenElseExp_strategy = st.builds(
    fl_IfThenElseExp,
)
fl_ArgumentExp_strategy = st.builds(
    fl_ArgumentExp,
)
fl_ApplyExp_strategy = st.builds(
    fl_ApplyExp,
)
fl_LiteralExp_strategy = st.builds(
    fl_LiteralExp,
    value=
        st.integers()
)
fl_Exp_strategy = st.builds(
    fl_Exp,
)
fl_Argument_strategy = st.builds(
    fl_Argument,
    name=
        safe_text
)
fl_Function_strategy = st.builds(
    fl_Function,
    name=
        safe_text
)
fl_Program_strategy = st.builds(
    fl_Program,
)
fl_BinaryExp_strategy = st.builds(
    fl_BinaryExp,
)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=fl_MinusExp_strategy)
@settings(max_examples=50)
def test_fl_minusexp_instantiation(instance):
    assert isinstance(instance, fl_MinusExp)

@given(instance=fl_EqualExp_strategy)
@settings(max_examples=50)
def test_fl_equalexp_instantiation(instance):
    assert isinstance(instance, fl_EqualExp)

@given(instance=fl_PlusExp_strategy)
@settings(max_examples=50)
def test_fl_plusexp_instantiation(instance):
    assert isinstance(instance, fl_PlusExp)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=fl_IfThenElseExp_strategy)
@settings(max_examples=50)
def test_fl_ifthenelseexp_instantiation(instance):
    assert isinstance(instance, fl_IfThenElseExp)

@given(instance=fl_ArgumentExp_strategy)
@settings(max_examples=50)
def test_fl_argumentexp_instantiation(instance):
    assert isinstance(instance, fl_ArgumentExp)

@given(instance=fl_ApplyExp_strategy)
@settings(max_examples=50)
def test_fl_applyexp_instantiation(instance):
    assert isinstance(instance, fl_ApplyExp)

@given(instance=fl_LiteralExp_strategy)
@settings(max_examples=50)
def test_fl_literalexp_instantiation(instance):
    assert isinstance(instance, fl_LiteralExp)



@given(instance=fl_LiteralExp_strategy)
def test_fl_literalexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fl_Exp_strategy)
@settings(max_examples=50)
def test_fl_exp_instantiation(instance):
    assert isinstance(instance, fl_Exp)

@given(instance=fl_Argument_strategy)
@settings(max_examples=50)
def test_fl_argument_instantiation(instance):
    assert isinstance(instance, fl_Argument)



@given(instance=fl_Argument_strategy)
def test_fl_argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl_Function_strategy)
@settings(max_examples=50)
def test_fl_function_instantiation(instance):
    assert isinstance(instance, fl_Function)



@given(instance=fl_Function_strategy)
def test_fl_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl_Program_strategy)
@settings(max_examples=50)
def test_fl_program_instantiation(instance):
    assert isinstance(instance, fl_Program)

@given(instance=fl_BinaryExp_strategy)
@settings(max_examples=50)
def test_fl_binaryexp_instantiation(instance):
    assert isinstance(instance, fl_BinaryExp)
