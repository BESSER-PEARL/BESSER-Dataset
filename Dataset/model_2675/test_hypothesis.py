import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    refs_Named,
    Named,
    refs_E,
    refs_B,
    refs_H,
    refs_C,
    refs_G,
    refs_F,
    refs_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refs_named_is_not_abstract():
    assert not inspect.isabstract(refs_Named)


def test_refs_named_constructor_exists():
    assert callable(refs_Named.__init__)


def test_refs_named_constructor_args():
    sig = inspect.signature(refs_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refs_named_has_name():
    assert hasattr(refs_Named, "name")
    descriptor = None
    for klass in refs_Named.__mro__:
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



def test_refs_e_is_not_abstract():
    assert not inspect.isabstract(refs_E)


def test_refs_e_constructor_exists():
    assert callable(refs_E.__init__)


def test_refs_e_constructor_args():
    sig = inspect.signature(refs_E.__init__)
    params = list(sig.parameters.keys())



def test_refs_b_is_not_abstract():
    assert not inspect.isabstract(refs_B)


def test_refs_b_constructor_exists():
    assert callable(refs_B.__init__)


def test_refs_b_constructor_args():
    sig = inspect.signature(refs_B.__init__)
    params = list(sig.parameters.keys())



def test_refs_h_is_not_abstract():
    assert not inspect.isabstract(refs_H)


def test_refs_h_constructor_exists():
    assert callable(refs_H.__init__)


def test_refs_h_constructor_args():
    sig = inspect.signature(refs_H.__init__)
    params = list(sig.parameters.keys())



def test_refs_c_is_not_abstract():
    assert not inspect.isabstract(refs_C)


def test_refs_c_constructor_exists():
    assert callable(refs_C.__init__)


def test_refs_c_constructor_args():
    sig = inspect.signature(refs_C.__init__)
    params = list(sig.parameters.keys())



def test_refs_g_is_not_abstract():
    assert not inspect.isabstract(refs_G)


def test_refs_g_constructor_exists():
    assert callable(refs_G.__init__)


def test_refs_g_constructor_args():
    sig = inspect.signature(refs_G.__init__)
    params = list(sig.parameters.keys())



def test_refs_f_is_not_abstract():
    assert not inspect.isabstract(refs_F)


def test_refs_f_constructor_exists():
    assert callable(refs_F.__init__)


def test_refs_f_constructor_args():
    sig = inspect.signature(refs_F.__init__)
    params = list(sig.parameters.keys())



def test_refs_a_is_not_abstract():
    assert not inspect.isabstract(refs_A)


def test_refs_a_constructor_exists():
    assert callable(refs_A.__init__)


def test_refs_a_constructor_args():
    sig = inspect.signature(refs_A.__init__)
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
refs_Named_strategy = st.builds(
    refs_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
refs_E_strategy = st.builds(
    refs_E,
)
refs_B_strategy = st.builds(
    refs_B,
)
refs_H_strategy = st.builds(
    refs_H,
)
refs_C_strategy = st.builds(
    refs_C,
)
refs_G_strategy = st.builds(
    refs_G,
)
refs_F_strategy = st.builds(
    refs_F,
)
refs_A_strategy = st.builds(
    refs_A,
)

@given(instance=refs_Named_strategy)
@settings(max_examples=50)
def test_refs_named_instantiation(instance):
    assert isinstance(instance, refs_Named)



@given(instance=refs_Named_strategy)
def test_refs_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=refs_E_strategy)
@settings(max_examples=50)
def test_refs_e_instantiation(instance):
    assert isinstance(instance, refs_E)

@given(instance=refs_B_strategy)
@settings(max_examples=50)
def test_refs_b_instantiation(instance):
    assert isinstance(instance, refs_B)

@given(instance=refs_H_strategy)
@settings(max_examples=50)
def test_refs_h_instantiation(instance):
    assert isinstance(instance, refs_H)

@given(instance=refs_C_strategy)
@settings(max_examples=50)
def test_refs_c_instantiation(instance):
    assert isinstance(instance, refs_C)

@given(instance=refs_G_strategy)
@settings(max_examples=50)
def test_refs_g_instantiation(instance):
    assert isinstance(instance, refs_G)

@given(instance=refs_F_strategy)
@settings(max_examples=50)
def test_refs_f_instantiation(instance):
    assert isinstance(instance, refs_F)

@given(instance=refs_A_strategy)
@settings(max_examples=50)
def test_refs_a_instantiation(instance):
    assert isinstance(instance, refs_A)
