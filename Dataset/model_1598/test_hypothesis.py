import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    Petrinet_Place,
    Petrinet_Transition,
    Arc,
    Petrinet_InputArc,
    Petrinet_OutputArc,
    Element,
    Petrinet_Arc,
    Petrinet_Node,
    Petrinet_Petrinet,
    Petrinet_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(Petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(Petrinet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(Petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(Petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "minDelay" in params, "Missing parameter 'minDelay'"
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"

def test_petrinet_transition_has_minDelay():
    assert hasattr(Petrinet_Transition, "minDelay")
    descriptor = None
    for klass in Petrinet_Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_maxDelay():
    assert hasattr(Petrinet_Transition, "maxDelay")
    descriptor = None
    for klass in Petrinet_Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_inputarc_is_not_abstract():
    assert not inspect.isabstract(Petrinet_InputArc)


def test_petrinet_inputarc_constructor_exists():
    assert callable(Petrinet_InputArc.__init__)


def test_petrinet_inputarc_constructor_args():
    sig = inspect.signature(Petrinet_InputArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_outputarc_is_not_abstract():
    assert not inspect.isabstract(Petrinet_OutputArc)


def test_petrinet_outputarc_constructor_exists():
    assert callable(Petrinet_OutputArc.__init__)


def test_petrinet_outputarc_constructor_args():
    sig = inspect.signature(Petrinet_OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(Petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(Petrinet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(Petrinet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(Petrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Petrinet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(Petrinet_Petrinet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(Petrinet_Petrinet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(Petrinet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(Petrinet_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_element_has_name():
    assert hasattr(Petrinet_Element, "name")
    descriptor = None
    for klass in Petrinet_Element.__mro__:
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
Node_strategy = st.builds(
    Node,
)
Petrinet_Place_strategy = st.builds(
    Petrinet_Place,
)
Petrinet_Transition_strategy = st.builds(
    Petrinet_Transition,
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Arc_strategy = st.builds(
    Arc,
)
Petrinet_InputArc_strategy = st.builds(
    Petrinet_InputArc,
)
Petrinet_OutputArc_strategy = st.builds(
    Petrinet_OutputArc,
)
Element_strategy = st.builds(
    Element,
)
Petrinet_Arc_strategy = st.builds(
    Petrinet_Arc,
)
Petrinet_Node_strategy = st.builds(
    Petrinet_Node,
)
Petrinet_Petrinet_strategy = st.builds(
    Petrinet_Petrinet,
)
Petrinet_Element_strategy = st.builds(
    Petrinet_Element,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, Petrinet_Place)

@given(instance=Petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, Petrinet_Transition)



@given(instance=Petrinet_Transition_strategy)
def test_petrinet_transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original



@given(instance=Petrinet_Transition_strategy)
def test_petrinet_transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=Petrinet_InputArc_strategy)
@settings(max_examples=50)
def test_petrinet_inputarc_instantiation(instance):
    assert isinstance(instance, Petrinet_InputArc)

@given(instance=Petrinet_OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet_outputarc_instantiation(instance):
    assert isinstance(instance, Petrinet_OutputArc)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, Petrinet_Arc)

@given(instance=Petrinet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, Petrinet_Node)

@given(instance=Petrinet_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, Petrinet_Petrinet)

@given(instance=Petrinet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, Petrinet_Element)



@given(instance=Petrinet_Element_strategy)
def test_petrinet_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
