import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PathExp_State,
    Transition,
    State,
    Element,
    PathExp_Transition,
    PathExp_PathExp,
    PathExp_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pathexp_state_is_not_abstract():
    assert not inspect.isabstract(PathExp_State)


def test_pathexp_state_constructor_exists():
    assert callable(PathExp_State.__init__)


def test_pathexp_state_constructor_args():
    sig = inspect.signature(PathExp_State.__init__)
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



def test_pathexp_transition_is_not_abstract():
    assert not inspect.isabstract(PathExp_Transition)


def test_pathexp_transition_constructor_exists():
    assert callable(PathExp_Transition.__init__)


def test_pathexp_transition_constructor_args():
    sig = inspect.signature(PathExp_Transition.__init__)
    params = list(sig.parameters.keys())



def test_pathexp_pathexp_is_not_abstract():
    assert not inspect.isabstract(PathExp_PathExp)


def test_pathexp_pathexp_constructor_exists():
    assert callable(PathExp_PathExp.__init__)


def test_pathexp_pathexp_constructor_args():
    sig = inspect.signature(PathExp_PathExp.__init__)
    params = list(sig.parameters.keys())



def test_pathexp_element_is_not_abstract():
    assert not inspect.isabstract(PathExp_Element)


def test_pathexp_element_constructor_exists():
    assert callable(PathExp_Element.__init__)


def test_pathexp_element_constructor_args():
    sig = inspect.signature(PathExp_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pathexp_element_has_name():
    assert hasattr(PathExp_Element, "name")
    descriptor = None
    for klass in PathExp_Element.__mro__:
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
PathExp_State_strategy = st.builds(
    PathExp_State,
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
PathExp_Transition_strategy = st.builds(
    PathExp_Transition,
)
PathExp_PathExp_strategy = st.builds(
    PathExp_PathExp,
)
PathExp_Element_strategy = st.builds(
    PathExp_Element,
    name=
        safe_text
)

@given(instance=PathExp_State_strategy)
@settings(max_examples=50)
def test_pathexp_state_instantiation(instance):
    assert isinstance(instance, PathExp_State)

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

@given(instance=PathExp_Transition_strategy)
@settings(max_examples=50)
def test_pathexp_transition_instantiation(instance):
    assert isinstance(instance, PathExp_Transition)

@given(instance=PathExp_PathExp_strategy)
@settings(max_examples=50)
def test_pathexp_pathexp_instantiation(instance):
    assert isinstance(instance, PathExp_PathExp)

@given(instance=PathExp_Element_strategy)
@settings(max_examples=50)
def test_pathexp_element_instantiation(instance):
    assert isinstance(instance, PathExp_Element)



@given(instance=PathExp_Element_strategy)
def test_pathexp_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
