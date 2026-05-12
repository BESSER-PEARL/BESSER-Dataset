import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hfsmReq_NamedElement,
    NamedElement,
    hfsmReq_AbstractState,
    hfsmReq_Transition,
    hfsmReq_Region,
    AbstractState,
    hfsmReq_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hfsmreq_namedelement_is_not_abstract():
    assert not inspect.isabstract(hfsmReq_NamedElement)


def test_hfsmreq_namedelement_constructor_exists():
    assert callable(hfsmReq_NamedElement.__init__)


def test_hfsmreq_namedelement_constructor_args():
    sig = inspect.signature(hfsmReq_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hfsmreq_namedelement_has_name():
    assert hasattr(hfsmReq_NamedElement, "name")
    descriptor = None
    for klass in hfsmReq_NamedElement.__mro__:
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



def test_hfsmreq_abstractstate_is_not_abstract():
    assert not inspect.isabstract(hfsmReq_AbstractState)


def test_hfsmreq_abstractstate_constructor_exists():
    assert callable(hfsmReq_AbstractState.__init__)


def test_hfsmreq_abstractstate_constructor_args():
    sig = inspect.signature(hfsmReq_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsmreq_transition_is_not_abstract():
    assert not inspect.isabstract(hfsmReq_Transition)


def test_hfsmreq_transition_constructor_exists():
    assert callable(hfsmReq_Transition.__init__)


def test_hfsmreq_transition_constructor_args():
    sig = inspect.signature(hfsmReq_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hfsmreq_region_is_not_abstract():
    assert not inspect.isabstract(hfsmReq_Region)


def test_hfsmreq_region_constructor_exists():
    assert callable(hfsmReq_Region.__init__)


def test_hfsmreq_region_constructor_args():
    sig = inspect.signature(hfsmReq_Region.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hfsmreq_state_is_not_abstract():
    assert not inspect.isabstract(hfsmReq_State)


def test_hfsmreq_state_constructor_exists():
    assert callable(hfsmReq_State.__init__)


def test_hfsmreq_state_constructor_args():
    sig = inspect.signature(hfsmReq_State.__init__)
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
hfsmReq_NamedElement_strategy = st.builds(
    hfsmReq_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hfsmReq_AbstractState_strategy = st.builds(
    hfsmReq_AbstractState,
)
hfsmReq_Transition_strategy = st.builds(
    hfsmReq_Transition,
)
hfsmReq_Region_strategy = st.builds(
    hfsmReq_Region,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hfsmReq_State_strategy = st.builds(
    hfsmReq_State,
)

@given(instance=hfsmReq_NamedElement_strategy)
@settings(max_examples=50)
def test_hfsmreq_namedelement_instantiation(instance):
    assert isinstance(instance, hfsmReq_NamedElement)



@given(instance=hfsmReq_NamedElement_strategy)
def test_hfsmreq_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hfsmReq_AbstractState_strategy)
@settings(max_examples=50)
def test_hfsmreq_abstractstate_instantiation(instance):
    assert isinstance(instance, hfsmReq_AbstractState)

@given(instance=hfsmReq_Transition_strategy)
@settings(max_examples=50)
def test_hfsmreq_transition_instantiation(instance):
    assert isinstance(instance, hfsmReq_Transition)

@given(instance=hfsmReq_Region_strategy)
@settings(max_examples=50)
def test_hfsmreq_region_instantiation(instance):
    assert isinstance(instance, hfsmReq_Region)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=hfsmReq_State_strategy)
@settings(max_examples=50)
def test_hfsmreq_state_instantiation(instance):
    assert isinstance(instance, hfsmReq_State)
