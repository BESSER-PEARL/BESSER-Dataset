import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    conts::Named,
    Named,
    conts::H,
    conts::B,
    conts::F,
    conts::G,
    conts::E,
    conts::C,
    conts::A,
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



def test_conts::named_is_not_abstract():
    assert not inspect.isabstract(conts::Named)


def test_conts::named_constructor_exists():
    assert callable(conts::Named.__init__)


def test_conts::named_constructor_args():
    sig = inspect.signature(conts::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conts::named_has_name():
    assert hasattr(conts::Named, "name")
    descriptor = None
    for klass in conts::Named.__mro__:
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



def test_conts::h_is_not_abstract():
    assert not inspect.isabstract(conts::H)


def test_conts::h_constructor_exists():
    assert callable(conts::H.__init__)


def test_conts::h_constructor_args():
    sig = inspect.signature(conts::H.__init__)
    params = list(sig.parameters.keys())



def test_conts::b_is_not_abstract():
    assert not inspect.isabstract(conts::B)


def test_conts::b_constructor_exists():
    assert callable(conts::B.__init__)


def test_conts::b_constructor_args():
    sig = inspect.signature(conts::B.__init__)
    params = list(sig.parameters.keys())



def test_conts::f_is_not_abstract():
    assert not inspect.isabstract(conts::F)


def test_conts::f_constructor_exists():
    assert callable(conts::F.__init__)


def test_conts::f_constructor_args():
    sig = inspect.signature(conts::F.__init__)
    params = list(sig.parameters.keys())



def test_conts::g_is_not_abstract():
    assert not inspect.isabstract(conts::G)


def test_conts::g_constructor_exists():
    assert callable(conts::G.__init__)


def test_conts::g_constructor_args():
    sig = inspect.signature(conts::G.__init__)
    params = list(sig.parameters.keys())



def test_conts::e_is_not_abstract():
    assert not inspect.isabstract(conts::E)


def test_conts::e_constructor_exists():
    assert callable(conts::E.__init__)


def test_conts::e_constructor_args():
    sig = inspect.signature(conts::E.__init__)
    params = list(sig.parameters.keys())



def test_conts::c_is_not_abstract():
    assert not inspect.isabstract(conts::C)


def test_conts::c_constructor_exists():
    assert callable(conts::C.__init__)


def test_conts::c_constructor_args():
    sig = inspect.signature(conts::C.__init__)
    params = list(sig.parameters.keys())



def test_conts::a_is_not_abstract():
    assert not inspect.isabstract(conts::A)


def test_conts::a_constructor_exists():
    assert callable(conts::A.__init__)


def test_conts::a_constructor_args():
    sig = inspect.signature(conts::A.__init__)
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
conts::Named_strategy = st.builds(
    conts::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
conts::H_strategy = st.builds(
    conts::H,
)
conts::B_strategy = st.builds(
    conts::B,
)
conts::F_strategy = st.builds(
    conts::F,
)
conts::G_strategy = st.builds(
    conts::G,
)
conts::E_strategy = st.builds(
    conts::E,
)
conts::C_strategy = st.builds(
    conts::C,
)
conts::A_strategy = st.builds(
    conts::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=conts::Named_strategy)
@settings(max_examples=50)
def test_conts::named_instantiation(instance):
    assert isinstance(instance, conts::Named)

@given(instance=conts::Named_strategy)
def test_conts::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conts::Named_strategy)
def test_conts::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=conts::H_strategy)
@settings(max_examples=50)
def test_conts::h_instantiation(instance):
    assert isinstance(instance, conts::H)

@given(instance=conts::B_strategy)
@settings(max_examples=50)
def test_conts::b_instantiation(instance):
    assert isinstance(instance, conts::B)

@given(instance=conts::F_strategy)
@settings(max_examples=50)
def test_conts::f_instantiation(instance):
    assert isinstance(instance, conts::F)

@given(instance=conts::G_strategy)
@settings(max_examples=50)
def test_conts::g_instantiation(instance):
    assert isinstance(instance, conts::G)

@given(instance=conts::E_strategy)
@settings(max_examples=50)
def test_conts::e_instantiation(instance):
    assert isinstance(instance, conts::E)

@given(instance=conts::C_strategy)
@settings(max_examples=50)
def test_conts::c_instantiation(instance):
    assert isinstance(instance, conts::C)

@given(instance=conts::A_strategy)
@settings(max_examples=50)
def test_conts::a_instantiation(instance):
    assert isinstance(instance, conts::A)
