import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    refact::Named,
    refact::A,
    Named,
    refact::C,
    refact::E,
    refact::D,
    refact::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refact::named_is_not_abstract():
    assert not inspect.isabstract(refact::Named)


def test_refact::named_constructor_exists():
    assert callable(refact::Named.__init__)


def test_refact::named_constructor_args():
    sig = inspect.signature(refact::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refact::named_has_name():
    assert hasattr(refact::Named, "name")
    descriptor = None
    for klass in refact::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refact::a_is_not_abstract():
    assert not inspect.isabstract(refact::A)


def test_refact::a_constructor_exists():
    assert callable(refact::A.__init__)


def test_refact::a_constructor_args():
    sig = inspect.signature(refact::A.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_refact::c_is_not_abstract():
    assert not inspect.isabstract(refact::C)


def test_refact::c_constructor_exists():
    assert callable(refact::C.__init__)


def test_refact::c_constructor_args():
    sig = inspect.signature(refact::C.__init__)
    params = list(sig.parameters.keys())



def test_refact::e_is_not_abstract():
    assert not inspect.isabstract(refact::E)


def test_refact::e_constructor_exists():
    assert callable(refact::E.__init__)


def test_refact::e_constructor_args():
    sig = inspect.signature(refact::E.__init__)
    params = list(sig.parameters.keys())



def test_refact::d_is_not_abstract():
    assert not inspect.isabstract(refact::D)


def test_refact::d_constructor_exists():
    assert callable(refact::D.__init__)


def test_refact::d_constructor_args():
    sig = inspect.signature(refact::D.__init__)
    params = list(sig.parameters.keys())



def test_refact::b_is_not_abstract():
    assert not inspect.isabstract(refact::B)


def test_refact::b_constructor_exists():
    assert callable(refact::B.__init__)


def test_refact::b_constructor_args():
    sig = inspect.signature(refact::B.__init__)
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
refact::Named_strategy = st.builds(
    refact::Named,
    name=
        safe_text
)
refact::A_strategy = st.builds(
    refact::A,
)
Named_strategy = st.builds(
    Named,
)
refact::C_strategy = st.builds(
    refact::C,
)
refact::E_strategy = st.builds(
    refact::E,
)
refact::D_strategy = st.builds(
    refact::D,
)
refact::B_strategy = st.builds(
    refact::B,
)

@given(instance=refact::Named_strategy)
@settings(max_examples=50)
def test_refact::named_instantiation(instance):
    assert isinstance(instance, refact::Named)

@given(instance=refact::Named_strategy)
def test_refact::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=refact::Named_strategy)
def test_refact::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refact::A_strategy)
@settings(max_examples=50)
def test_refact::a_instantiation(instance):
    assert isinstance(instance, refact::A)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=refact::C_strategy)
@settings(max_examples=50)
def test_refact::c_instantiation(instance):
    assert isinstance(instance, refact::C)

@given(instance=refact::E_strategy)
@settings(max_examples=50)
def test_refact::e_instantiation(instance):
    assert isinstance(instance, refact::E)

@given(instance=refact::D_strategy)
@settings(max_examples=50)
def test_refact::d_instantiation(instance):
    assert isinstance(instance, refact::D)

@given(instance=refact::B_strategy)
@settings(max_examples=50)
def test_refact::b_instantiation(instance):
    assert isinstance(instance, refact::B)
