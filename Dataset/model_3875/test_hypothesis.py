import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExp,
    fl::EqualExp,
    fl::MinusExp,
    fl::PlusExp,
    Exp,
    fl::ArgumentExp,
    fl::IfThenElseExp,
    fl::LiteralExp,
    fl::Exp,
    fl::Argument,
    fl::Function,
    fl::Program,
    fl::BinaryExp,
    fl::ApplyExp,
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



def test_fl::equalexp_is_not_abstract():
    assert not inspect.isabstract(fl::EqualExp)


def test_fl::equalexp_constructor_exists():
    assert callable(fl::EqualExp.__init__)


def test_fl::equalexp_constructor_args():
    sig = inspect.signature(fl::EqualExp.__init__)
    params = list(sig.parameters.keys())



def test_fl::minusexp_is_not_abstract():
    assert not inspect.isabstract(fl::MinusExp)


def test_fl::minusexp_constructor_exists():
    assert callable(fl::MinusExp.__init__)


def test_fl::minusexp_constructor_args():
    sig = inspect.signature(fl::MinusExp.__init__)
    params = list(sig.parameters.keys())



def test_fl::plusexp_is_not_abstract():
    assert not inspect.isabstract(fl::PlusExp)


def test_fl::plusexp_constructor_exists():
    assert callable(fl::PlusExp.__init__)


def test_fl::plusexp_constructor_args():
    sig = inspect.signature(fl::PlusExp.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_fl::argumentexp_is_not_abstract():
    assert not inspect.isabstract(fl::ArgumentExp)


def test_fl::argumentexp_constructor_exists():
    assert callable(fl::ArgumentExp.__init__)


def test_fl::argumentexp_constructor_args():
    sig = inspect.signature(fl::ArgumentExp.__init__)
    params = list(sig.parameters.keys())



def test_fl::ifthenelseexp_is_not_abstract():
    assert not inspect.isabstract(fl::IfThenElseExp)


def test_fl::ifthenelseexp_constructor_exists():
    assert callable(fl::IfThenElseExp.__init__)


def test_fl::ifthenelseexp_constructor_args():
    sig = inspect.signature(fl::IfThenElseExp.__init__)
    params = list(sig.parameters.keys())



def test_fl::literalexp_is_not_abstract():
    assert not inspect.isabstract(fl::LiteralExp)


def test_fl::literalexp_constructor_exists():
    assert callable(fl::LiteralExp.__init__)


def test_fl::literalexp_constructor_args():
    sig = inspect.signature(fl::LiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fl::literalexp_has_value():
    assert hasattr(fl::LiteralExp, "value")
    descriptor = None
    for klass in fl::LiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fl::exp_is_not_abstract():
    assert not inspect.isabstract(fl::Exp)


def test_fl::exp_constructor_exists():
    assert callable(fl::Exp.__init__)


def test_fl::exp_constructor_args():
    sig = inspect.signature(fl::Exp.__init__)
    params = list(sig.parameters.keys())



def test_fl::argument_is_not_abstract():
    assert not inspect.isabstract(fl::Argument)


def test_fl::argument_constructor_exists():
    assert callable(fl::Argument.__init__)


def test_fl::argument_constructor_args():
    sig = inspect.signature(fl::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl::argument_has_name():
    assert hasattr(fl::Argument, "name")
    descriptor = None
    for klass in fl::Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl::function_is_not_abstract():
    assert not inspect.isabstract(fl::Function)


def test_fl::function_constructor_exists():
    assert callable(fl::Function.__init__)


def test_fl::function_constructor_args():
    sig = inspect.signature(fl::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fl::function_has_name():
    assert hasattr(fl::Function, "name")
    descriptor = None
    for klass in fl::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fl::program_is_not_abstract():
    assert not inspect.isabstract(fl::Program)


def test_fl::program_constructor_exists():
    assert callable(fl::Program.__init__)


def test_fl::program_constructor_args():
    sig = inspect.signature(fl::Program.__init__)
    params = list(sig.parameters.keys())



def test_fl::binaryexp_is_not_abstract():
    assert not inspect.isabstract(fl::BinaryExp)


def test_fl::binaryexp_constructor_exists():
    assert callable(fl::BinaryExp.__init__)


def test_fl::binaryexp_constructor_args():
    sig = inspect.signature(fl::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_fl::applyexp_is_not_abstract():
    assert not inspect.isabstract(fl::ApplyExp)


def test_fl::applyexp_constructor_exists():
    assert callable(fl::ApplyExp.__init__)


def test_fl::applyexp_constructor_args():
    sig = inspect.signature(fl::ApplyExp.__init__)
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
fl::EqualExp_strategy = st.builds(
    fl::EqualExp,
)
fl::MinusExp_strategy = st.builds(
    fl::MinusExp,
)
fl::PlusExp_strategy = st.builds(
    fl::PlusExp,
)
Exp_strategy = st.builds(
    Exp,
)
fl::ArgumentExp_strategy = st.builds(
    fl::ArgumentExp,
)
fl::IfThenElseExp_strategy = st.builds(
    fl::IfThenElseExp,
)
fl::LiteralExp_strategy = st.builds(
    fl::LiteralExp,
    value=
        st.integers()
)
fl::Exp_strategy = st.builds(
    fl::Exp,
)
fl::Argument_strategy = st.builds(
    fl::Argument,
    name=
        safe_text
)
fl::Function_strategy = st.builds(
    fl::Function,
    name=
        safe_text
)
fl::Program_strategy = st.builds(
    fl::Program,
)
fl::BinaryExp_strategy = st.builds(
    fl::BinaryExp,
)
fl::ApplyExp_strategy = st.builds(
    fl::ApplyExp,
)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=fl::EqualExp_strategy)
@settings(max_examples=50)
def test_fl::equalexp_instantiation(instance):
    assert isinstance(instance, fl::EqualExp)

@given(instance=fl::MinusExp_strategy)
@settings(max_examples=50)
def test_fl::minusexp_instantiation(instance):
    assert isinstance(instance, fl::MinusExp)

@given(instance=fl::PlusExp_strategy)
@settings(max_examples=50)
def test_fl::plusexp_instantiation(instance):
    assert isinstance(instance, fl::PlusExp)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=fl::ArgumentExp_strategy)
@settings(max_examples=50)
def test_fl::argumentexp_instantiation(instance):
    assert isinstance(instance, fl::ArgumentExp)

@given(instance=fl::IfThenElseExp_strategy)
@settings(max_examples=50)
def test_fl::ifthenelseexp_instantiation(instance):
    assert isinstance(instance, fl::IfThenElseExp)

@given(instance=fl::LiteralExp_strategy)
@settings(max_examples=50)
def test_fl::literalexp_instantiation(instance):
    assert isinstance(instance, fl::LiteralExp)

@given(instance=fl::LiteralExp_strategy)
def test_fl::literalexp_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fl::LiteralExp_strategy)
def test_fl::literalexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fl::Exp_strategy)
@settings(max_examples=50)
def test_fl::exp_instantiation(instance):
    assert isinstance(instance, fl::Exp)

@given(instance=fl::Argument_strategy)
@settings(max_examples=50)
def test_fl::argument_instantiation(instance):
    assert isinstance(instance, fl::Argument)

@given(instance=fl::Argument_strategy)
def test_fl::argument_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fl::Argument_strategy)
def test_fl::argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl::Function_strategy)
@settings(max_examples=50)
def test_fl::function_instantiation(instance):
    assert isinstance(instance, fl::Function)

@given(instance=fl::Function_strategy)
def test_fl::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fl::Function_strategy)
def test_fl::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fl::Program_strategy)
@settings(max_examples=50)
def test_fl::program_instantiation(instance):
    assert isinstance(instance, fl::Program)

@given(instance=fl::BinaryExp_strategy)
@settings(max_examples=50)
def test_fl::binaryexp_instantiation(instance):
    assert isinstance(instance, fl::BinaryExp)

@given(instance=fl::ApplyExp_strategy)
@settings(max_examples=50)
def test_fl::applyexp_instantiation(instance):
    assert isinstance(instance, fl::ApplyExp)
