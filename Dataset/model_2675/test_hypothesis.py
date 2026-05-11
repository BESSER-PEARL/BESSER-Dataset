import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    refs::Named,
    Named,
    refs::F,
    refs::C,
    refs::G,
    refs::E,
    refs::B,
    refs::H,
    refs::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refs::named_is_not_abstract():
    assert not inspect.isabstract(refs::Named)


def test_refs::named_constructor_exists():
    assert callable(refs::Named.__init__)


def test_refs::named_constructor_args():
    sig = inspect.signature(refs::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refs::named_has_name():
    assert hasattr(refs::Named, "name")
    descriptor = None
    for klass in refs::Named.__mro__:
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



def test_refs::f_is_not_abstract():
    assert not inspect.isabstract(refs::F)


def test_refs::f_constructor_exists():
    assert callable(refs::F.__init__)


def test_refs::f_constructor_args():
    sig = inspect.signature(refs::F.__init__)
    params = list(sig.parameters.keys())



def test_refs::c_is_not_abstract():
    assert not inspect.isabstract(refs::C)


def test_refs::c_constructor_exists():
    assert callable(refs::C.__init__)


def test_refs::c_constructor_args():
    sig = inspect.signature(refs::C.__init__)
    params = list(sig.parameters.keys())



def test_refs::g_is_not_abstract():
    assert not inspect.isabstract(refs::G)


def test_refs::g_constructor_exists():
    assert callable(refs::G.__init__)


def test_refs::g_constructor_args():
    sig = inspect.signature(refs::G.__init__)
    params = list(sig.parameters.keys())



def test_refs::e_is_not_abstract():
    assert not inspect.isabstract(refs::E)


def test_refs::e_constructor_exists():
    assert callable(refs::E.__init__)


def test_refs::e_constructor_args():
    sig = inspect.signature(refs::E.__init__)
    params = list(sig.parameters.keys())



def test_refs::b_is_not_abstract():
    assert not inspect.isabstract(refs::B)


def test_refs::b_constructor_exists():
    assert callable(refs::B.__init__)


def test_refs::b_constructor_args():
    sig = inspect.signature(refs::B.__init__)
    params = list(sig.parameters.keys())



def test_refs::h_is_not_abstract():
    assert not inspect.isabstract(refs::H)


def test_refs::h_constructor_exists():
    assert callable(refs::H.__init__)


def test_refs::h_constructor_args():
    sig = inspect.signature(refs::H.__init__)
    params = list(sig.parameters.keys())



def test_refs::a_is_not_abstract():
    assert not inspect.isabstract(refs::A)


def test_refs::a_constructor_exists():
    assert callable(refs::A.__init__)


def test_refs::a_constructor_args():
    sig = inspect.signature(refs::A.__init__)
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
refs::Named_strategy = st.builds(
    refs::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
refs::F_strategy = st.builds(
    refs::F,
)
refs::C_strategy = st.builds(
    refs::C,
)
refs::G_strategy = st.builds(
    refs::G,
)
refs::E_strategy = st.builds(
    refs::E,
)
refs::B_strategy = st.builds(
    refs::B,
)
refs::H_strategy = st.builds(
    refs::H,
)
refs::A_strategy = st.builds(
    refs::A,
)

@given(instance=refs::Named_strategy)
@settings(max_examples=50)
def test_refs::named_instantiation(instance):
    assert isinstance(instance, refs::Named)

@given(instance=refs::Named_strategy)
def test_refs::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=refs::Named_strategy)
def test_refs::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=refs::F_strategy)
@settings(max_examples=50)
def test_refs::f_instantiation(instance):
    assert isinstance(instance, refs::F)

@given(instance=refs::C_strategy)
@settings(max_examples=50)
def test_refs::c_instantiation(instance):
    assert isinstance(instance, refs::C)

@given(instance=refs::G_strategy)
@settings(max_examples=50)
def test_refs::g_instantiation(instance):
    assert isinstance(instance, refs::G)

@given(instance=refs::E_strategy)
@settings(max_examples=50)
def test_refs::e_instantiation(instance):
    assert isinstance(instance, refs::E)

@given(instance=refs::B_strategy)
@settings(max_examples=50)
def test_refs::b_instantiation(instance):
    assert isinstance(instance, refs::B)

@given(instance=refs::H_strategy)
@settings(max_examples=50)
def test_refs::h_instantiation(instance):
    assert isinstance(instance, refs::H)

@given(instance=refs::A_strategy)
@settings(max_examples=50)
def test_refs::a_instantiation(instance):
    assert isinstance(instance, refs::A)
