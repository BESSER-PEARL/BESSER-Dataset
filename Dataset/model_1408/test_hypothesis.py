import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hfsm_NamedElement,
    NamedElement,
    hfsm_AbstractState,
    hfsm_Region,
    AbstractState,
    hfsm_State,
    hfsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hfsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(hfsm_NamedElement)


def test_hfsm_namedelement_constructor_exists():
    assert callable(hfsm_NamedElement.__init__)


def test_hfsm_namedelement_constructor_args():
    sig = inspect.signature(hfsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hfsm_namedelement_has_name():
    assert hasattr(hfsm_NamedElement, "name")
    descriptor = None
    for klass in hfsm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hfsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(hfsm_AbstractState)


def test_hfsm_abstractstate_constructor_exists():
    assert callable(hfsm_AbstractState.__init__)


def test_hfsm_abstractstate_constructor_args():
    sig = inspect.signature(hfsm_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsm_region_is_not_abstract():
    assert not inspect.isabstract(hfsm_Region)


def test_hfsm_region_constructor_exists():
    assert callable(hfsm_Region.__init__)


def test_hfsm_region_constructor_args():
    sig = inspect.signature(hfsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsm_state_is_not_abstract():
    assert not inspect.isabstract(hfsm_State)


def test_hfsm_state_constructor_exists():
    assert callable(hfsm_State.__init__)


def test_hfsm_state_constructor_args():
    sig = inspect.signature(hfsm_State.__init__)
    params = list(sig.parameters.keys())



def test_hfsm_transition_is_not_abstract():
    assert not inspect.isabstract(hfsm_Transition)


def test_hfsm_transition_constructor_exists():
    assert callable(hfsm_Transition.__init__)


def test_hfsm_transition_constructor_args():
    sig = inspect.signature(hfsm_Transition.__init__)
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
hfsm_NamedElement_strategy = st.builds(
    hfsm_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hfsm_AbstractState_strategy = st.builds(
    hfsm_AbstractState,
)
hfsm_Region_strategy = st.builds(
    hfsm_Region,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hfsm_State_strategy = st.builds(
    hfsm_State,
)
hfsm_Transition_strategy = st.builds(
    hfsm_Transition,
)

@given(instance=hfsm_NamedElement_strategy)
@settings(max_examples=50)
def test_hfsm_namedelement_instantiation(instance):
    assert isinstance(instance, hfsm_NamedElement)



@given(instance=hfsm_NamedElement_strategy)
def test_hfsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hfsm_AbstractState_strategy)
@settings(max_examples=50)
def test_hfsm_abstractstate_instantiation(instance):
    assert isinstance(instance, hfsm_AbstractState)

@given(instance=hfsm_Region_strategy)
@settings(max_examples=50)
def test_hfsm_region_instantiation(instance):
    assert isinstance(instance, hfsm_Region)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=hfsm_State_strategy)
@settings(max_examples=50)
def test_hfsm_state_instantiation(instance):
    assert isinstance(instance, hfsm_State)

@given(instance=hfsm_Transition_strategy)
@settings(max_examples=50)
def test_hfsm_transition_instantiation(instance):
    assert isinstance(instance, hfsm_Transition)
