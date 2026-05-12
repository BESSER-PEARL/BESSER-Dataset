import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    abc_NamedElement,
    NamedElement,
    abc_B,
    abc_C,
    abc_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc_namedelement_is_not_abstract():
    assert not inspect.isabstract(abc_NamedElement)


def test_abc_namedelement_constructor_exists():
    assert callable(abc_NamedElement.__init__)


def test_abc_namedelement_constructor_args():
    sig = inspect.signature(abc_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abc_namedelement_has_name():
    assert hasattr(abc_NamedElement, "name")
    descriptor = None
    for klass in abc_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_abc_b_is_not_abstract():
    assert not inspect.isabstract(abc_B)


def test_abc_b_constructor_exists():
    assert callable(abc_B.__init__)


def test_abc_b_constructor_args():
    sig = inspect.signature(abc_B.__init__)
    params = list(sig.parameters.keys())



def test_abc_c_is_not_abstract():
    assert not inspect.isabstract(abc_C)


def test_abc_c_constructor_exists():
    assert callable(abc_C.__init__)


def test_abc_c_constructor_args():
    sig = inspect.signature(abc_C.__init__)
    params = list(sig.parameters.keys())



def test_abc_a_is_not_abstract():
    assert not inspect.isabstract(abc_A)


def test_abc_a_constructor_exists():
    assert callable(abc_A.__init__)


def test_abc_a_constructor_args():
    sig = inspect.signature(abc_A.__init__)
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
abc_NamedElement_strategy = st.builds(
    abc_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
abc_B_strategy = st.builds(
    abc_B,
)
abc_C_strategy = st.builds(
    abc_C,
)
abc_A_strategy = st.builds(
    abc_A,
)

@given(instance=abc_NamedElement_strategy)
@settings(max_examples=50)
def test_abc_namedelement_instantiation(instance):
    assert isinstance(instance, abc_NamedElement)



@given(instance=abc_NamedElement_strategy)
def test_abc_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=abc_B_strategy)
@settings(max_examples=50)
def test_abc_b_instantiation(instance):
    assert isinstance(instance, abc_B)

@given(instance=abc_C_strategy)
@settings(max_examples=50)
def test_abc_c_instantiation(instance):
    assert isinstance(instance, abc_C)

@given(instance=abc_A_strategy)
@settings(max_examples=50)
def test_abc_a_instantiation(instance):
    assert isinstance(instance, abc_A)
