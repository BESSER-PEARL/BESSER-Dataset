import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet_NamedElement,
    Edge,
    petrinet_ReadEdge,
    petrinet_InhibitorEdge,
    petrinet_OutputEdge,
    petrinet_InputEdge,
    NamedElement,
    petrinet_PetriNet,
    petrinet_Edge,
    petrinet_Transition,
    petrinet_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_readedge_is_not_abstract():
    assert not inspect.isabstract(petrinet_ReadEdge)


def test_petrinet_readedge_constructor_exists():
    assert callable(petrinet_ReadEdge.__init__)


def test_petrinet_readedge_constructor_args():
    sig = inspect.signature(petrinet_ReadEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_inhibitoredge_is_not_abstract():
    assert not inspect.isabstract(petrinet_InhibitorEdge)


def test_petrinet_inhibitoredge_constructor_exists():
    assert callable(petrinet_InhibitorEdge.__init__)


def test_petrinet_inhibitoredge_constructor_args():
    sig = inspect.signature(petrinet_InhibitorEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_outputedge_is_not_abstract():
    assert not inspect.isabstract(petrinet_OutputEdge)


def test_petrinet_outputedge_constructor_exists():
    assert callable(petrinet_OutputEdge.__init__)


def test_petrinet_outputedge_constructor_args():
    sig = inspect.signature(petrinet_OutputEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_inputedge_is_not_abstract():
    assert not inspect.isabstract(petrinet_InputEdge)


def test_petrinet_inputedge_constructor_exists():
    assert callable(petrinet_InputEdge.__init__)


def test_petrinet_inputedge_constructor_args():
    sig = inspect.signature(petrinet_InputEdge.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_edge_is_not_abstract():
    assert not inspect.isabstract(petrinet_Edge)


def test_petrinet_edge_constructor_exists():
    assert callable(petrinet_Edge.__init__)


def test_petrinet_edge_constructor_args():
    sig = inspect.signature(petrinet_Edge.__init__)
    params = list(sig.parameters.keys())



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
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinet_place_has_tokens():
    assert hasattr(petrinet_Place, "tokens")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
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
petrinet_NamedElement_strategy = st.builds(
    petrinet_NamedElement,
    name=
        safe_text
)
Edge_strategy = st.builds(
    Edge,
)
petrinet_ReadEdge_strategy = st.builds(
    petrinet_ReadEdge,
)
petrinet_InhibitorEdge_strategy = st.builds(
    petrinet_InhibitorEdge,
)
petrinet_OutputEdge_strategy = st.builds(
    petrinet_OutputEdge,
)
petrinet_InputEdge_strategy = st.builds(
    petrinet_InputEdge,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
)
petrinet_Edge_strategy = st.builds(
    petrinet_Edge,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    tokens=
        st.integers()
)

@given(instance=petrinet_NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet_namedelement_instantiation(instance):
    assert isinstance(instance, petrinet_NamedElement)



@given(instance=petrinet_NamedElement_strategy)
def test_petrinet_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=petrinet_ReadEdge_strategy)
@settings(max_examples=50)
def test_petrinet_readedge_instantiation(instance):
    assert isinstance(instance, petrinet_ReadEdge)

@given(instance=petrinet_InhibitorEdge_strategy)
@settings(max_examples=50)
def test_petrinet_inhibitoredge_instantiation(instance):
    assert isinstance(instance, petrinet_InhibitorEdge)

@given(instance=petrinet_OutputEdge_strategy)
@settings(max_examples=50)
def test_petrinet_outputedge_instantiation(instance):
    assert isinstance(instance, petrinet_OutputEdge)

@given(instance=petrinet_InputEdge_strategy)
@settings(max_examples=50)
def test_petrinet_inputedge_instantiation(instance):
    assert isinstance(instance, petrinet_InputEdge)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)

@given(instance=petrinet_Edge_strategy)
@settings(max_examples=50)
def test_petrinet_edge_instantiation(instance):
    assert isinstance(instance, petrinet_Edge)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original
