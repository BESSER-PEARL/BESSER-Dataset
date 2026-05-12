import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    reference_Named,
    Named,
    reference_B,
    reference_E,
    reference_C,
    reference_F,
    reference_H,
    reference_G,
    reference_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reference_named_is_not_abstract():
    assert not inspect.isabstract(reference_Named)


def test_reference_named_constructor_exists():
    assert callable(reference_Named.__init__)


def test_reference_named_constructor_args():
    sig = inspect.signature(reference_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_reference_named_has_name():
    assert hasattr(reference_Named, "name")
    descriptor = None
    for klass in reference_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_reference_b_is_not_abstract():
    assert not inspect.isabstract(reference_B)


def test_reference_b_constructor_exists():
    assert callable(reference_B.__init__)


def test_reference_b_constructor_args():
    sig = inspect.signature(reference_B.__init__)
    params = list(sig.parameters.keys())



def test_reference_e_is_not_abstract():
    assert not inspect.isabstract(reference_E)


def test_reference_e_constructor_exists():
    assert callable(reference_E.__init__)


def test_reference_e_constructor_args():
    sig = inspect.signature(reference_E.__init__)
    params = list(sig.parameters.keys())



def test_reference_c_is_not_abstract():
    assert not inspect.isabstract(reference_C)


def test_reference_c_constructor_exists():
    assert callable(reference_C.__init__)


def test_reference_c_constructor_args():
    sig = inspect.signature(reference_C.__init__)
    params = list(sig.parameters.keys())



def test_reference_f_is_not_abstract():
    assert not inspect.isabstract(reference_F)


def test_reference_f_constructor_exists():
    assert callable(reference_F.__init__)


def test_reference_f_constructor_args():
    sig = inspect.signature(reference_F.__init__)
    params = list(sig.parameters.keys())



def test_reference_h_is_not_abstract():
    assert not inspect.isabstract(reference_H)


def test_reference_h_constructor_exists():
    assert callable(reference_H.__init__)


def test_reference_h_constructor_args():
    sig = inspect.signature(reference_H.__init__)
    params = list(sig.parameters.keys())



def test_reference_g_is_not_abstract():
    assert not inspect.isabstract(reference_G)


def test_reference_g_constructor_exists():
    assert callable(reference_G.__init__)


def test_reference_g_constructor_args():
    sig = inspect.signature(reference_G.__init__)
    params = list(sig.parameters.keys())



def test_reference_a_is_not_abstract():
    assert not inspect.isabstract(reference_A)


def test_reference_a_constructor_exists():
    assert callable(reference_A.__init__)


def test_reference_a_constructor_args():
    sig = inspect.signature(reference_A.__init__)
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
reference_Named_strategy = st.builds(
    reference_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
reference_B_strategy = st.builds(
    reference_B,
)
reference_E_strategy = st.builds(
    reference_E,
)
reference_C_strategy = st.builds(
    reference_C,
)
reference_F_strategy = st.builds(
    reference_F,
)
reference_H_strategy = st.builds(
    reference_H,
)
reference_G_strategy = st.builds(
    reference_G,
)
reference_A_strategy = st.builds(
    reference_A,
)

@given(instance=reference_Named_strategy)
@settings(max_examples=50)
def test_reference_named_instantiation(instance):
    assert isinstance(instance, reference_Named)



@given(instance=reference_Named_strategy)
def test_reference_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=reference_B_strategy)
@settings(max_examples=50)
def test_reference_b_instantiation(instance):
    assert isinstance(instance, reference_B)

@given(instance=reference_E_strategy)
@settings(max_examples=50)
def test_reference_e_instantiation(instance):
    assert isinstance(instance, reference_E)

@given(instance=reference_C_strategy)
@settings(max_examples=50)
def test_reference_c_instantiation(instance):
    assert isinstance(instance, reference_C)

@given(instance=reference_F_strategy)
@settings(max_examples=50)
def test_reference_f_instantiation(instance):
    assert isinstance(instance, reference_F)

@given(instance=reference_H_strategy)
@settings(max_examples=50)
def test_reference_h_instantiation(instance):
    assert isinstance(instance, reference_H)

@given(instance=reference_G_strategy)
@settings(max_examples=50)
def test_reference_g_instantiation(instance):
    assert isinstance(instance, reference_G)

@given(instance=reference_A_strategy)
@settings(max_examples=50)
def test_reference_a_instantiation(instance):
    assert isinstance(instance, reference_A)
