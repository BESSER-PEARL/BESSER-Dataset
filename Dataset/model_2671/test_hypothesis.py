import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    comps_Named,
    Named,
    comps_F,
    comps_G,
    comps_B,
    comps_H,
    comps_C,
    comps_E,
    comps_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_comps_named_is_not_abstract():
    assert not inspect.isabstract(comps_Named)


def test_comps_named_constructor_exists():
    assert callable(comps_Named.__init__)


def test_comps_named_constructor_args():
    sig = inspect.signature(comps_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_comps_named_has_name():
    assert hasattr(comps_Named, "name")
    descriptor = None
    for klass in comps_Named.__mro__:
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



def test_comps_f_is_not_abstract():
    assert not inspect.isabstract(comps_F)


def test_comps_f_constructor_exists():
    assert callable(comps_F.__init__)


def test_comps_f_constructor_args():
    sig = inspect.signature(comps_F.__init__)
    params = list(sig.parameters.keys())



def test_comps_g_is_not_abstract():
    assert not inspect.isabstract(comps_G)


def test_comps_g_constructor_exists():
    assert callable(comps_G.__init__)


def test_comps_g_constructor_args():
    sig = inspect.signature(comps_G.__init__)
    params = list(sig.parameters.keys())



def test_comps_b_is_not_abstract():
    assert not inspect.isabstract(comps_B)


def test_comps_b_constructor_exists():
    assert callable(comps_B.__init__)


def test_comps_b_constructor_args():
    sig = inspect.signature(comps_B.__init__)
    params = list(sig.parameters.keys())



def test_comps_h_is_not_abstract():
    assert not inspect.isabstract(comps_H)


def test_comps_h_constructor_exists():
    assert callable(comps_H.__init__)


def test_comps_h_constructor_args():
    sig = inspect.signature(comps_H.__init__)
    params = list(sig.parameters.keys())



def test_comps_c_is_not_abstract():
    assert not inspect.isabstract(comps_C)


def test_comps_c_constructor_exists():
    assert callable(comps_C.__init__)


def test_comps_c_constructor_args():
    sig = inspect.signature(comps_C.__init__)
    params = list(sig.parameters.keys())



def test_comps_e_is_not_abstract():
    assert not inspect.isabstract(comps_E)


def test_comps_e_constructor_exists():
    assert callable(comps_E.__init__)


def test_comps_e_constructor_args():
    sig = inspect.signature(comps_E.__init__)
    params = list(sig.parameters.keys())



def test_comps_a_is_not_abstract():
    assert not inspect.isabstract(comps_A)


def test_comps_a_constructor_exists():
    assert callable(comps_A.__init__)


def test_comps_a_constructor_args():
    sig = inspect.signature(comps_A.__init__)
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
B_strategy = st.builds(
    B,
)
comps_Named_strategy = st.builds(
    comps_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
comps_F_strategy = st.builds(
    comps_F,
)
comps_G_strategy = st.builds(
    comps_G,
)
comps_B_strategy = st.builds(
    comps_B,
)
comps_H_strategy = st.builds(
    comps_H,
)
comps_C_strategy = st.builds(
    comps_C,
)
comps_E_strategy = st.builds(
    comps_E,
)
comps_A_strategy = st.builds(
    comps_A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=comps_Named_strategy)
@settings(max_examples=50)
def test_comps_named_instantiation(instance):
    assert isinstance(instance, comps_Named)



@given(instance=comps_Named_strategy)
def test_comps_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=comps_F_strategy)
@settings(max_examples=50)
def test_comps_f_instantiation(instance):
    assert isinstance(instance, comps_F)

@given(instance=comps_G_strategy)
@settings(max_examples=50)
def test_comps_g_instantiation(instance):
    assert isinstance(instance, comps_G)

@given(instance=comps_B_strategy)
@settings(max_examples=50)
def test_comps_b_instantiation(instance):
    assert isinstance(instance, comps_B)

@given(instance=comps_H_strategy)
@settings(max_examples=50)
def test_comps_h_instantiation(instance):
    assert isinstance(instance, comps_H)

@given(instance=comps_C_strategy)
@settings(max_examples=50)
def test_comps_c_instantiation(instance):
    assert isinstance(instance, comps_C)

@given(instance=comps_E_strategy)
@settings(max_examples=50)
def test_comps_e_instantiation(instance):
    assert isinstance(instance, comps_E)

@given(instance=comps_A_strategy)
@settings(max_examples=50)
def test_comps_a_instantiation(instance):
    assert isinstance(instance, comps_A)
