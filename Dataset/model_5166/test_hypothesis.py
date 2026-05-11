import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RootIn,
    in::B,
    in::A,
    in::RootIn,
    in::RootContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rootin_is_not_abstract():
    assert not inspect.isabstract(RootIn)


def test_rootin_constructor_exists():
    assert callable(RootIn.__init__)


def test_rootin_constructor_args():
    sig = inspect.signature(RootIn.__init__)
    params = list(sig.parameters.keys())



def test_in::b_is_not_abstract():
    assert not inspect.isabstract(in::B)


def test_in::b_constructor_exists():
    assert callable(in::B.__init__)


def test_in::b_constructor_args():
    sig = inspect.signature(in::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_in::b_has_name():
    assert hasattr(in::B, "name")
    descriptor = None
    for klass in in::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_in::a_is_not_abstract():
    assert not inspect.isabstract(in::A)


def test_in::a_constructor_exists():
    assert callable(in::A.__init__)


def test_in::a_constructor_args():
    sig = inspect.signature(in::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_in::a_has_name():
    assert hasattr(in::A, "name")
    descriptor = None
    for klass in in::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_in::rootin_is_not_abstract():
    assert not inspect.isabstract(in::RootIn)


def test_in::rootin_constructor_exists():
    assert callable(in::RootIn.__init__)


def test_in::rootin_constructor_args():
    sig = inspect.signature(in::RootIn.__init__)
    params = list(sig.parameters.keys())



def test_in::rootcontainer_is_not_abstract():
    assert not inspect.isabstract(in::RootContainer)


def test_in::rootcontainer_constructor_exists():
    assert callable(in::RootContainer.__init__)


def test_in::rootcontainer_constructor_args():
    sig = inspect.signature(in::RootContainer.__init__)
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
RootIn_strategy = st.builds(
    RootIn,
)
in::B_strategy = st.builds(
    in::B,
    name=
        safe_text
)
in::A_strategy = st.builds(
    in::A,
    name=
        safe_text
)
in::RootIn_strategy = st.builds(
    in::RootIn,
)
in::RootContainer_strategy = st.builds(
    in::RootContainer,
)

@given(instance=RootIn_strategy)
@settings(max_examples=50)
def test_rootin_instantiation(instance):
    assert isinstance(instance, RootIn)

@given(instance=in::B_strategy)
@settings(max_examples=50)
def test_in::b_instantiation(instance):
    assert isinstance(instance, in::B)

@given(instance=in::B_strategy)
def test_in::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=in::B_strategy)
def test_in::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=in::A_strategy)
@settings(max_examples=50)
def test_in::a_instantiation(instance):
    assert isinstance(instance, in::A)

@given(instance=in::A_strategy)
def test_in::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=in::A_strategy)
def test_in::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=in::RootIn_strategy)
@settings(max_examples=50)
def test_in::rootin_instantiation(instance):
    assert isinstance(instance, in::RootIn)

@given(instance=in::RootContainer_strategy)
@settings(max_examples=50)
def test_in::rootcontainer_instantiation(instance):
    assert isinstance(instance, in::RootContainer)
