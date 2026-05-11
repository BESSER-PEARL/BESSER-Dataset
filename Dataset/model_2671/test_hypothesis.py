import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    comps::Named,
    Named,
    comps::B,
    comps::C,
    comps::E,
    comps::H,
    comps::F,
    comps::G,
    comps::A,
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



def test_comps::named_is_not_abstract():
    assert not inspect.isabstract(comps::Named)


def test_comps::named_constructor_exists():
    assert callable(comps::Named.__init__)


def test_comps::named_constructor_args():
    sig = inspect.signature(comps::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_comps::named_has_name():
    assert hasattr(comps::Named, "name")
    descriptor = None
    for klass in comps::Named.__mro__:
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



def test_comps::b_is_not_abstract():
    assert not inspect.isabstract(comps::B)


def test_comps::b_constructor_exists():
    assert callable(comps::B.__init__)


def test_comps::b_constructor_args():
    sig = inspect.signature(comps::B.__init__)
    params = list(sig.parameters.keys())



def test_comps::c_is_not_abstract():
    assert not inspect.isabstract(comps::C)


def test_comps::c_constructor_exists():
    assert callable(comps::C.__init__)


def test_comps::c_constructor_args():
    sig = inspect.signature(comps::C.__init__)
    params = list(sig.parameters.keys())



def test_comps::e_is_not_abstract():
    assert not inspect.isabstract(comps::E)


def test_comps::e_constructor_exists():
    assert callable(comps::E.__init__)


def test_comps::e_constructor_args():
    sig = inspect.signature(comps::E.__init__)
    params = list(sig.parameters.keys())



def test_comps::h_is_not_abstract():
    assert not inspect.isabstract(comps::H)


def test_comps::h_constructor_exists():
    assert callable(comps::H.__init__)


def test_comps::h_constructor_args():
    sig = inspect.signature(comps::H.__init__)
    params = list(sig.parameters.keys())



def test_comps::f_is_not_abstract():
    assert not inspect.isabstract(comps::F)


def test_comps::f_constructor_exists():
    assert callable(comps::F.__init__)


def test_comps::f_constructor_args():
    sig = inspect.signature(comps::F.__init__)
    params = list(sig.parameters.keys())



def test_comps::g_is_not_abstract():
    assert not inspect.isabstract(comps::G)


def test_comps::g_constructor_exists():
    assert callable(comps::G.__init__)


def test_comps::g_constructor_args():
    sig = inspect.signature(comps::G.__init__)
    params = list(sig.parameters.keys())



def test_comps::a_is_not_abstract():
    assert not inspect.isabstract(comps::A)


def test_comps::a_constructor_exists():
    assert callable(comps::A.__init__)


def test_comps::a_constructor_args():
    sig = inspect.signature(comps::A.__init__)
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
comps::Named_strategy = st.builds(
    comps::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
comps::B_strategy = st.builds(
    comps::B,
)
comps::C_strategy = st.builds(
    comps::C,
)
comps::E_strategy = st.builds(
    comps::E,
)
comps::H_strategy = st.builds(
    comps::H,
)
comps::F_strategy = st.builds(
    comps::F,
)
comps::G_strategy = st.builds(
    comps::G,
)
comps::A_strategy = st.builds(
    comps::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=comps::Named_strategy)
@settings(max_examples=50)
def test_comps::named_instantiation(instance):
    assert isinstance(instance, comps::Named)

@given(instance=comps::Named_strategy)
def test_comps::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=comps::Named_strategy)
def test_comps::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=comps::B_strategy)
@settings(max_examples=50)
def test_comps::b_instantiation(instance):
    assert isinstance(instance, comps::B)

@given(instance=comps::C_strategy)
@settings(max_examples=50)
def test_comps::c_instantiation(instance):
    assert isinstance(instance, comps::C)

@given(instance=comps::E_strategy)
@settings(max_examples=50)
def test_comps::e_instantiation(instance):
    assert isinstance(instance, comps::E)

@given(instance=comps::H_strategy)
@settings(max_examples=50)
def test_comps::h_instantiation(instance):
    assert isinstance(instance, comps::H)

@given(instance=comps::F_strategy)
@settings(max_examples=50)
def test_comps::f_instantiation(instance):
    assert isinstance(instance, comps::F)

@given(instance=comps::G_strategy)
@settings(max_examples=50)
def test_comps::g_instantiation(instance):
    assert isinstance(instance, comps::G)

@given(instance=comps::A_strategy)
@settings(max_examples=50)
def test_comps::a_instantiation(instance):
    assert isinstance(instance, comps::A)
