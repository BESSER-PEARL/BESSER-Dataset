import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hfsmReq::NamedElement,
    NamedElement,
    hfsmReq::AbstractState,
    hfsmReq::Transition,
    hfsmReq::Region,
    AbstractState,
    hfsmReq::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hfsmreq::namedelement_is_not_abstract():
    assert not inspect.isabstract(hfsmReq::NamedElement)


def test_hfsmreq::namedelement_constructor_exists():
    assert callable(hfsmReq::NamedElement.__init__)


def test_hfsmreq::namedelement_constructor_args():
    sig = inspect.signature(hfsmReq::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hfsmreq::namedelement_has_name():
    assert hasattr(hfsmReq::NamedElement, "name")
    descriptor = None
    for klass in hfsmReq::NamedElement.__mro__:
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



def test_hfsmreq::abstractstate_is_not_abstract():
    assert not inspect.isabstract(hfsmReq::AbstractState)


def test_hfsmreq::abstractstate_constructor_exists():
    assert callable(hfsmReq::AbstractState.__init__)


def test_hfsmreq::abstractstate_constructor_args():
    sig = inspect.signature(hfsmReq::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsmreq::transition_is_not_abstract():
    assert not inspect.isabstract(hfsmReq::Transition)


def test_hfsmreq::transition_constructor_exists():
    assert callable(hfsmReq::Transition.__init__)


def test_hfsmreq::transition_constructor_args():
    sig = inspect.signature(hfsmReq::Transition.__init__)
    params = list(sig.parameters.keys())



def test_hfsmreq::region_is_not_abstract():
    assert not inspect.isabstract(hfsmReq::Region)


def test_hfsmreq::region_constructor_exists():
    assert callable(hfsmReq::Region.__init__)


def test_hfsmreq::region_constructor_args():
    sig = inspect.signature(hfsmReq::Region.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsmreq::state_is_not_abstract():
    assert not inspect.isabstract(hfsmReq::State)


def test_hfsmreq::state_constructor_exists():
    assert callable(hfsmReq::State.__init__)


def test_hfsmreq::state_constructor_args():
    sig = inspect.signature(hfsmReq::State.__init__)
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
hfsmReq::NamedElement_strategy = st.builds(
    hfsmReq::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hfsmReq::AbstractState_strategy = st.builds(
    hfsmReq::AbstractState,
)
hfsmReq::Transition_strategy = st.builds(
    hfsmReq::Transition,
)
hfsmReq::Region_strategy = st.builds(
    hfsmReq::Region,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hfsmReq::State_strategy = st.builds(
    hfsmReq::State,
)

@given(instance=hfsmReq::NamedElement_strategy)
@settings(max_examples=50)
def test_hfsmreq::namedelement_instantiation(instance):
    assert isinstance(instance, hfsmReq::NamedElement)

@given(instance=hfsmReq::NamedElement_strategy)
def test_hfsmreq::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hfsmReq::NamedElement_strategy)
def test_hfsmreq::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hfsmReq::AbstractState_strategy)
@settings(max_examples=50)
def test_hfsmreq::abstractstate_instantiation(instance):
    assert isinstance(instance, hfsmReq::AbstractState)

@given(instance=hfsmReq::Transition_strategy)
@settings(max_examples=50)
def test_hfsmreq::transition_instantiation(instance):
    assert isinstance(instance, hfsmReq::Transition)

@given(instance=hfsmReq::Region_strategy)
@settings(max_examples=50)
def test_hfsmreq::region_instantiation(instance):
    assert isinstance(instance, hfsmReq::Region)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=hfsmReq::State_strategy)
@settings(max_examples=50)
def test_hfsmreq::state_instantiation(instance):
    assert isinstance(instance, hfsmReq::State)
