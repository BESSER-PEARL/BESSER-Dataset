import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    petrinet_NamedElement,
    petrinet_Transition,
    petrinet_Place,
    petrinet_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_namedelement_is_not_abstract():
    assert not inspect.isabstract(petrinet_NamedElement)


def test_petrinet_namedelement_constructor_exists():
    assert callable(petrinet_NamedElement.__init__)


def test_petrinet_namedelement_constructor_args():
    sig = inspect.signature(petrinet_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_namedelement_has_name():
    assert hasattr(petrinet_NamedElement, "name")
    descriptor = None
    for klass in petrinet_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(petrinet_Net)


def test_petrinet_net_constructor_exists():
    assert callable(petrinet_Net.__init__)


def test_petrinet_net_constructor_args():
    sig = inspect.signature(petrinet_Net.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
petrinet_NamedElement_strategy = st.builds(
    petrinet_NamedElement,
    name=
        safe_text
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
)
petrinet_Net_strategy = st.builds(
    petrinet_Net,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petrinet_NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet_namedelement_instantiation(instance):
    assert isinstance(instance, petrinet_NamedElement)



@given(instance=petrinet_NamedElement_strategy)
def test_petrinet_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)

@given(instance=petrinet_Net_strategy)
@settings(max_examples=50)
def test_petrinet_net_instantiation(instance):
    assert isinstance(instance, petrinet_Net)
