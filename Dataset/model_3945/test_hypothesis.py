import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PathExp,
    PathExp::State,
    Transition,
    State,
    Element,
    PathExp::Transition,
    PathExp::PathExp,
    PathExp::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pathexp_is_not_abstract():
    assert not inspect.isabstract(PathExp)


def test_pathexp_constructor_exists():
    assert callable(PathExp.__init__)


def test_pathexp_constructor_args():
    sig = inspect.signature(PathExp.__init__)
    params = list(sig.parameters.keys())



def test_pathexp::state_is_not_abstract():
    assert not inspect.isabstract(PathExp::State)


def test_pathexp::state_constructor_exists():
    assert callable(PathExp::State.__init__)


def test_pathexp::state_constructor_args():
    sig = inspect.signature(PathExp::State.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_pathexp::transition_is_not_abstract():
    assert not inspect.isabstract(PathExp::Transition)


def test_pathexp::transition_constructor_exists():
    assert callable(PathExp::Transition.__init__)


def test_pathexp::transition_constructor_args():
    sig = inspect.signature(PathExp::Transition.__init__)
    params = list(sig.parameters.keys())



def test_pathexp::pathexp_is_not_abstract():
    assert not inspect.isabstract(PathExp::PathExp)


def test_pathexp::pathexp_constructor_exists():
    assert callable(PathExp::PathExp.__init__)


def test_pathexp::pathexp_constructor_args():
    sig = inspect.signature(PathExp::PathExp.__init__)
    params = list(sig.parameters.keys())



def test_pathexp::element_is_not_abstract():
    assert not inspect.isabstract(PathExp::Element)


def test_pathexp::element_constructor_exists():
    assert callable(PathExp::Element.__init__)


def test_pathexp::element_constructor_args():
    sig = inspect.signature(PathExp::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pathexp::element_has_name():
    assert hasattr(PathExp::Element, "name")
    descriptor = None
    for klass in PathExp::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
PathExp_strategy = st.builds(
    PathExp,
)
PathExp::State_strategy = st.builds(
    PathExp::State,
)
Transition_strategy = st.builds(
    Transition,
)
State_strategy = st.builds(
    State,
)
Element_strategy = st.builds(
    Element,
)
PathExp::Transition_strategy = st.builds(
    PathExp::Transition,
)
PathExp::PathExp_strategy = st.builds(
    PathExp::PathExp,
)
PathExp::Element_strategy = st.builds(
    PathExp::Element,
    name=
        safe_text
)

@given(instance=PathExp_strategy)
@settings(max_examples=50)
def test_pathexp_instantiation(instance):
    assert isinstance(instance, PathExp)

@given(instance=PathExp::State_strategy)
@settings(max_examples=50)
def test_pathexp::state_instantiation(instance):
    assert isinstance(instance, PathExp::State)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PathExp::Transition_strategy)
@settings(max_examples=50)
def test_pathexp::transition_instantiation(instance):
    assert isinstance(instance, PathExp::Transition)

@given(instance=PathExp::PathExp_strategy)
@settings(max_examples=50)
def test_pathexp::pathexp_instantiation(instance):
    assert isinstance(instance, PathExp::PathExp)

@given(instance=PathExp::Element_strategy)
@settings(max_examples=50)
def test_pathexp::element_instantiation(instance):
    assert isinstance(instance, PathExp::Element)

@given(instance=PathExp::Element_strategy)
def test_pathexp::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PathExp::Element_strategy)
def test_pathexp::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
