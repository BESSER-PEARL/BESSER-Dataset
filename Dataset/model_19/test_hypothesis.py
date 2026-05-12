import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet2_Element,
    petrinet2_Petrinet,
    Node,
    petrinet2_Transition,
    petrinet2_Place,
    Element,
    petrinet2_Arc,
    petrinet2_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet2_element_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Element)


def test_petrinet2_element_constructor_exists():
    assert callable(petrinet2_Element.__init__)


def test_petrinet2_element_constructor_args():
    sig = inspect.signature(petrinet2_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2_element_has_name():
    assert hasattr(petrinet2_Element, "name")
    descriptor = None
    for klass in petrinet2_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Petrinet)


def test_petrinet2_petrinet_constructor_exists():
    assert callable(petrinet2_Petrinet.__init__)


def test_petrinet2_petrinet_constructor_args():
    sig = inspect.signature(petrinet2_Petrinet.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet2_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Transition)


def test_petrinet2_transition_constructor_exists():
    assert callable(petrinet2_Transition.__init__)


def test_petrinet2_transition_constructor_args():
    sig = inspect.signature(petrinet2_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "minDelay" in params, "Missing parameter 'minDelay'"
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"

def test_petrinet2_transition_has_minDelay():
    assert hasattr(petrinet2_Transition, "minDelay")
    descriptor = None
    for klass in petrinet2_Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet2_transition_has_maxDelay():
    assert hasattr(petrinet2_Transition, "maxDelay")
    descriptor = None
    for klass in petrinet2_Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2_place_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Place)


def test_petrinet2_place_constructor_exists():
    assert callable(petrinet2_Place.__init__)


def test_petrinet2_place_constructor_args():
    sig = inspect.signature(petrinet2_Place.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet2_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Arc)


def test_petrinet2_arc_constructor_exists():
    assert callable(petrinet2_Arc.__init__)


def test_petrinet2_arc_constructor_args():
    sig = inspect.signature(petrinet2_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet2_node_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Node)


def test_petrinet2_node_constructor_exists():
    assert callable(petrinet2_Node.__init__)


def test_petrinet2_node_constructor_args():
    sig = inspect.signature(petrinet2_Node.__init__)
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
petrinet2_Element_strategy = st.builds(
    petrinet2_Element,
    name=
        safe_text
)
petrinet2_Petrinet_strategy = st.builds(
    petrinet2_Petrinet,
)
Node_strategy = st.builds(
    Node,
)
petrinet2_Transition_strategy = st.builds(
    petrinet2_Transition,
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
petrinet2_Place_strategy = st.builds(
    petrinet2_Place,
)
Element_strategy = st.builds(
    Element,
)
petrinet2_Arc_strategy = st.builds(
    petrinet2_Arc,
)
petrinet2_Node_strategy = st.builds(
    petrinet2_Node,
)

@given(instance=petrinet2_Element_strategy)
@settings(max_examples=50)
def test_petrinet2_element_instantiation(instance):
    assert isinstance(instance, petrinet2_Element)



@given(instance=petrinet2_Element_strategy)
def test_petrinet2_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet2_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet2_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet2_Petrinet)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet2_Transition_strategy)
@settings(max_examples=50)
def test_petrinet2_transition_instantiation(instance):
    assert isinstance(instance, petrinet2_Transition)



@given(instance=petrinet2_Transition_strategy)
def test_petrinet2_transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original



@given(instance=petrinet2_Transition_strategy)
def test_petrinet2_transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original

@given(instance=petrinet2_Place_strategy)
@settings(max_examples=50)
def test_petrinet2_place_instantiation(instance):
    assert isinstance(instance, petrinet2_Place)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet2_Arc_strategy)
@settings(max_examples=50)
def test_petrinet2_arc_instantiation(instance):
    assert isinstance(instance, petrinet2_Arc)

@given(instance=petrinet2_Node_strategy)
@settings(max_examples=50)
def test_petrinet2_node_instantiation(instance):
    assert isinstance(instance, petrinet2_Node)
