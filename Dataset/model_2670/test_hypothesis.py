import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    conts_Named,
    Named,
    conts_C,
    conts_E,
    conts_B,
    conts_G,
    conts_F,
    conts_H,
    conts_A,
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



def test_conts_named_is_not_abstract():
    assert not inspect.isabstract(conts_Named)


def test_conts_named_constructor_exists():
    assert callable(conts_Named.__init__)


def test_conts_named_constructor_args():
    sig = inspect.signature(conts_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conts_named_has_name():
    assert hasattr(conts_Named, "name")
    descriptor = None
    for klass in conts_Named.__mro__:
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



def test_conts_c_is_not_abstract():
    assert not inspect.isabstract(conts_C)


def test_conts_c_constructor_exists():
    assert callable(conts_C.__init__)


def test_conts_c_constructor_args():
    sig = inspect.signature(conts_C.__init__)
    params = list(sig.parameters.keys())



def test_conts_e_is_not_abstract():
    assert not inspect.isabstract(conts_E)


def test_conts_e_constructor_exists():
    assert callable(conts_E.__init__)


def test_conts_e_constructor_args():
    sig = inspect.signature(conts_E.__init__)
    params = list(sig.parameters.keys())



def test_conts_b_is_not_abstract():
    assert not inspect.isabstract(conts_B)


def test_conts_b_constructor_exists():
    assert callable(conts_B.__init__)


def test_conts_b_constructor_args():
    sig = inspect.signature(conts_B.__init__)
    params = list(sig.parameters.keys())



def test_conts_g_is_not_abstract():
    assert not inspect.isabstract(conts_G)


def test_conts_g_constructor_exists():
    assert callable(conts_G.__init__)


def test_conts_g_constructor_args():
    sig = inspect.signature(conts_G.__init__)
    params = list(sig.parameters.keys())



def test_conts_f_is_not_abstract():
    assert not inspect.isabstract(conts_F)


def test_conts_f_constructor_exists():
    assert callable(conts_F.__init__)


def test_conts_f_constructor_args():
    sig = inspect.signature(conts_F.__init__)
    params = list(sig.parameters.keys())



def test_conts_h_is_not_abstract():
    assert not inspect.isabstract(conts_H)


def test_conts_h_constructor_exists():
    assert callable(conts_H.__init__)


def test_conts_h_constructor_args():
    sig = inspect.signature(conts_H.__init__)
    params = list(sig.parameters.keys())



def test_conts_a_is_not_abstract():
    assert not inspect.isabstract(conts_A)


def test_conts_a_constructor_exists():
    assert callable(conts_A.__init__)


def test_conts_a_constructor_args():
    sig = inspect.signature(conts_A.__init__)
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
conts_Named_strategy = st.builds(
    conts_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
conts_C_strategy = st.builds(
    conts_C,
)
conts_E_strategy = st.builds(
    conts_E,
)
conts_B_strategy = st.builds(
    conts_B,
)
conts_G_strategy = st.builds(
    conts_G,
)
conts_F_strategy = st.builds(
    conts_F,
)
conts_H_strategy = st.builds(
    conts_H,
)
conts_A_strategy = st.builds(
    conts_A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=conts_Named_strategy)
@settings(max_examples=50)
def test_conts_named_instantiation(instance):
    assert isinstance(instance, conts_Named)



@given(instance=conts_Named_strategy)
def test_conts_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=conts_C_strategy)
@settings(max_examples=50)
def test_conts_c_instantiation(instance):
    assert isinstance(instance, conts_C)

@given(instance=conts_E_strategy)
@settings(max_examples=50)
def test_conts_e_instantiation(instance):
    assert isinstance(instance, conts_E)

@given(instance=conts_B_strategy)
@settings(max_examples=50)
def test_conts_b_instantiation(instance):
    assert isinstance(instance, conts_B)

@given(instance=conts_G_strategy)
@settings(max_examples=50)
def test_conts_g_instantiation(instance):
    assert isinstance(instance, conts_G)

@given(instance=conts_F_strategy)
@settings(max_examples=50)
def test_conts_f_instantiation(instance):
    assert isinstance(instance, conts_F)

@given(instance=conts_H_strategy)
@settings(max_examples=50)
def test_conts_h_instantiation(instance):
    assert isinstance(instance, conts_H)

@given(instance=conts_A_strategy)
@settings(max_examples=50)
def test_conts_a_instantiation(instance):
    assert isinstance(instance, conts_A)
