import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    multiview::Named,
    Named,
    multiview::B,
    multiview::C,
    multiview::F,
    multiview::E,
    multiview::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multiview::named_is_not_abstract():
    assert not inspect.isabstract(multiview::Named)


def test_multiview::named_constructor_exists():
    assert callable(multiview::Named.__init__)


def test_multiview::named_constructor_args():
    sig = inspect.signature(multiview::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multiview::named_has_name():
    assert hasattr(multiview::Named, "name")
    descriptor = None
    for klass in multiview::Named.__mro__:
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



def test_multiview::b_is_not_abstract():
    assert not inspect.isabstract(multiview::B)


def test_multiview::b_constructor_exists():
    assert callable(multiview::B.__init__)


def test_multiview::b_constructor_args():
    sig = inspect.signature(multiview::B.__init__)
    params = list(sig.parameters.keys())



def test_multiview::c_is_not_abstract():
    assert not inspect.isabstract(multiview::C)


def test_multiview::c_constructor_exists():
    assert callable(multiview::C.__init__)


def test_multiview::c_constructor_args():
    sig = inspect.signature(multiview::C.__init__)
    params = list(sig.parameters.keys())



def test_multiview::f_is_not_abstract():
    assert not inspect.isabstract(multiview::F)


def test_multiview::f_constructor_exists():
    assert callable(multiview::F.__init__)


def test_multiview::f_constructor_args():
    sig = inspect.signature(multiview::F.__init__)
    params = list(sig.parameters.keys())



def test_multiview::e_is_not_abstract():
    assert not inspect.isabstract(multiview::E)


def test_multiview::e_constructor_exists():
    assert callable(multiview::E.__init__)


def test_multiview::e_constructor_args():
    sig = inspect.signature(multiview::E.__init__)
    params = list(sig.parameters.keys())



def test_multiview::a_is_not_abstract():
    assert not inspect.isabstract(multiview::A)


def test_multiview::a_constructor_exists():
    assert callable(multiview::A.__init__)


def test_multiview::a_constructor_args():
    sig = inspect.signature(multiview::A.__init__)
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
multiview::Named_strategy = st.builds(
    multiview::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
multiview::B_strategy = st.builds(
    multiview::B,
)
multiview::C_strategy = st.builds(
    multiview::C,
)
multiview::F_strategy = st.builds(
    multiview::F,
)
multiview::E_strategy = st.builds(
    multiview::E,
)
multiview::A_strategy = st.builds(
    multiview::A,
)

@given(instance=multiview::Named_strategy)
@settings(max_examples=50)
def test_multiview::named_instantiation(instance):
    assert isinstance(instance, multiview::Named)

@given(instance=multiview::Named_strategy)
def test_multiview::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=multiview::Named_strategy)
def test_multiview::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=multiview::B_strategy)
@settings(max_examples=50)
def test_multiview::b_instantiation(instance):
    assert isinstance(instance, multiview::B)

@given(instance=multiview::C_strategy)
@settings(max_examples=50)
def test_multiview::c_instantiation(instance):
    assert isinstance(instance, multiview::C)

@given(instance=multiview::F_strategy)
@settings(max_examples=50)
def test_multiview::f_instantiation(instance):
    assert isinstance(instance, multiview::F)

@given(instance=multiview::E_strategy)
@settings(max_examples=50)
def test_multiview::e_instantiation(instance):
    assert isinstance(instance, multiview::E)

@given(instance=multiview::A_strategy)
@settings(max_examples=50)
def test_multiview::a_instantiation(instance):
    assert isinstance(instance, multiview::A)
