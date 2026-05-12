import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    semlink_NamedElement,
    NamedElement,
    semlink_A,
    semlink_C,
    semlink_B,
    semlink_G,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_semlink_namedelement_is_not_abstract():
    assert not inspect.isabstract(semlink_NamedElement)


def test_semlink_namedelement_constructor_exists():
    assert callable(semlink_NamedElement.__init__)


def test_semlink_namedelement_constructor_args():
    sig = inspect.signature(semlink_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_semlink_namedelement_has_name():
    assert hasattr(semlink_NamedElement, "name")
    descriptor = None
    for klass in semlink_NamedElement.__mro__:
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



def test_semlink_a_is_not_abstract():
    assert not inspect.isabstract(semlink_A)


def test_semlink_a_constructor_exists():
    assert callable(semlink_A.__init__)


def test_semlink_a_constructor_args():
    sig = inspect.signature(semlink_A.__init__)
    params = list(sig.parameters.keys())



def test_semlink_c_is_not_abstract():
    assert not inspect.isabstract(semlink_C)


def test_semlink_c_constructor_exists():
    assert callable(semlink_C.__init__)


def test_semlink_c_constructor_args():
    sig = inspect.signature(semlink_C.__init__)
    params = list(sig.parameters.keys())



def test_semlink_b_is_not_abstract():
    assert not inspect.isabstract(semlink_B)


def test_semlink_b_constructor_exists():
    assert callable(semlink_B.__init__)


def test_semlink_b_constructor_args():
    sig = inspect.signature(semlink_B.__init__)
    params = list(sig.parameters.keys())



def test_semlink_g_is_not_abstract():
    assert not inspect.isabstract(semlink_G)


def test_semlink_g_constructor_exists():
    assert callable(semlink_G.__init__)


def test_semlink_g_constructor_args():
    sig = inspect.signature(semlink_G.__init__)
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
semlink_NamedElement_strategy = st.builds(
    semlink_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
semlink_A_strategy = st.builds(
    semlink_A,
)
semlink_C_strategy = st.builds(
    semlink_C,
)
semlink_B_strategy = st.builds(
    semlink_B,
)
semlink_G_strategy = st.builds(
    semlink_G,
)

@given(instance=semlink_NamedElement_strategy)
@settings(max_examples=50)
def test_semlink_namedelement_instantiation(instance):
    assert isinstance(instance, semlink_NamedElement)



@given(instance=semlink_NamedElement_strategy)
def test_semlink_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=semlink_A_strategy)
@settings(max_examples=50)
def test_semlink_a_instantiation(instance):
    assert isinstance(instance, semlink_A)

@given(instance=semlink_C_strategy)
@settings(max_examples=50)
def test_semlink_c_instantiation(instance):
    assert isinstance(instance, semlink_C)

@given(instance=semlink_B_strategy)
@settings(max_examples=50)
def test_semlink_b_instantiation(instance):
    assert isinstance(instance, semlink_B)

@given(instance=semlink_G_strategy)
@settings(max_examples=50)
def test_semlink_g_instantiation(instance):
    assert isinstance(instance, semlink_G)
