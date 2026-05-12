import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    refact_Named,
    refact_A,
    Named,
    refact_D,
    refact_B,
    refact_C,
    refact_E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refact_named_is_not_abstract():
    assert not inspect.isabstract(refact_Named)


def test_refact_named_constructor_exists():
    assert callable(refact_Named.__init__)


def test_refact_named_constructor_args():
    sig = inspect.signature(refact_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refact_named_has_name():
    assert hasattr(refact_Named, "name")
    descriptor = None
    for klass in refact_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refact_a_is_not_abstract():
    assert not inspect.isabstract(refact_A)


def test_refact_a_constructor_exists():
    assert callable(refact_A.__init__)


def test_refact_a_constructor_args():
    sig = inspect.signature(refact_A.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_refact_d_is_not_abstract():
    assert not inspect.isabstract(refact_D)


def test_refact_d_constructor_exists():
    assert callable(refact_D.__init__)


def test_refact_d_constructor_args():
    sig = inspect.signature(refact_D.__init__)
    params = list(sig.parameters.keys())



def test_refact_b_is_not_abstract():
    assert not inspect.isabstract(refact_B)


def test_refact_b_constructor_exists():
    assert callable(refact_B.__init__)


def test_refact_b_constructor_args():
    sig = inspect.signature(refact_B.__init__)
    params = list(sig.parameters.keys())



def test_refact_c_is_not_abstract():
    assert not inspect.isabstract(refact_C)


def test_refact_c_constructor_exists():
    assert callable(refact_C.__init__)


def test_refact_c_constructor_args():
    sig = inspect.signature(refact_C.__init__)
    params = list(sig.parameters.keys())



def test_refact_e_is_not_abstract():
    assert not inspect.isabstract(refact_E)


def test_refact_e_constructor_exists():
    assert callable(refact_E.__init__)


def test_refact_e_constructor_args():
    sig = inspect.signature(refact_E.__init__)
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
refact_Named_strategy = st.builds(
    refact_Named,
    name=
        safe_text
)
refact_A_strategy = st.builds(
    refact_A,
)
Named_strategy = st.builds(
    Named,
)
refact_D_strategy = st.builds(
    refact_D,
)
refact_B_strategy = st.builds(
    refact_B,
)
refact_C_strategy = st.builds(
    refact_C,
)
refact_E_strategy = st.builds(
    refact_E,
)

@given(instance=refact_Named_strategy)
@settings(max_examples=50)
def test_refact_named_instantiation(instance):
    assert isinstance(instance, refact_Named)



@given(instance=refact_Named_strategy)
def test_refact_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refact_A_strategy)
@settings(max_examples=50)
def test_refact_a_instantiation(instance):
    assert isinstance(instance, refact_A)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=refact_D_strategy)
@settings(max_examples=50)
def test_refact_d_instantiation(instance):
    assert isinstance(instance, refact_D)

@given(instance=refact_B_strategy)
@settings(max_examples=50)
def test_refact_b_instantiation(instance):
    assert isinstance(instance, refact_B)

@given(instance=refact_C_strategy)
@settings(max_examples=50)
def test_refact_c_instantiation(instance):
    assert isinstance(instance, refact_C)

@given(instance=refact_E_strategy)
@settings(max_examples=50)
def test_refact_e_instantiation(instance):
    assert isinstance(instance, refact_E)
