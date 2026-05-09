import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hfsm::NamedElement,
    NamedElement,
    hfsm::AbstractState,
    hfsm::Region,
    AbstractState,
    hfsm::State,
    hfsm::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hfsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(hfsm::NamedElement)


def test_hfsm::namedelement_constructor_exists():
    assert callable(hfsm::NamedElement.__init__)


def test_hfsm::namedelement_constructor_args():
    sig = inspect.signature(hfsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hfsm::namedelement_has_name():
    assert hasattr(hfsm::NamedElement, "name")
    descriptor = None
    for klass in hfsm::NamedElement.__mro__:
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



def test_hfsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(hfsm::AbstractState)


def test_hfsm::abstractstate_constructor_exists():
    assert callable(hfsm::AbstractState.__init__)


def test_hfsm::abstractstate_constructor_args():
    sig = inspect.signature(hfsm::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsm::region_is_not_abstract():
    assert not inspect.isabstract(hfsm::Region)


def test_hfsm::region_constructor_exists():
    assert callable(hfsm::Region.__init__)


def test_hfsm::region_constructor_args():
    sig = inspect.signature(hfsm::Region.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsm::state_is_not_abstract():
    assert not inspect.isabstract(hfsm::State)


def test_hfsm::state_constructor_exists():
    assert callable(hfsm::State.__init__)


def test_hfsm::state_constructor_args():
    sig = inspect.signature(hfsm::State.__init__)
    params = list(sig.parameters.keys())



def test_hfsm::transition_is_not_abstract():
    assert not inspect.isabstract(hfsm::Transition)


def test_hfsm::transition_constructor_exists():
    assert callable(hfsm::Transition.__init__)


def test_hfsm::transition_constructor_args():
    sig = inspect.signature(hfsm::Transition.__init__)
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
hfsm::NamedElement_strategy = st.builds(
    hfsm::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hfsm::AbstractState_strategy = st.builds(
    hfsm::AbstractState,
)
hfsm::Region_strategy = st.builds(
    hfsm::Region,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hfsm::State_strategy = st.builds(
    hfsm::State,
)
hfsm::Transition_strategy = st.builds(
    hfsm::Transition,
)

@given(instance=hfsm::NamedElement_strategy)
@settings(max_examples=50)
def test_hfsm::namedelement_instantiation(instance):
    assert isinstance(instance, hfsm::NamedElement)

@given(instance=hfsm::NamedElement_strategy)
def test_hfsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hfsm::NamedElement_strategy)
def test_hfsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hfsm::AbstractState_strategy)
@settings(max_examples=50)
def test_hfsm::abstractstate_instantiation(instance):
    assert isinstance(instance, hfsm::AbstractState)

@given(instance=hfsm::Region_strategy)
@settings(max_examples=50)
def test_hfsm::region_instantiation(instance):
    assert isinstance(instance, hfsm::Region)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=hfsm::State_strategy)
@settings(max_examples=50)
def test_hfsm::state_instantiation(instance):
    assert isinstance(instance, hfsm::State)

@given(instance=hfsm::Transition_strategy)
@settings(max_examples=50)
def test_hfsm::transition_instantiation(instance):
    assert isinstance(instance, hfsm::Transition)
