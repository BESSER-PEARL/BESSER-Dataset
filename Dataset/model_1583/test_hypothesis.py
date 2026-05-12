import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    petrinet_Place,
    petrinet_Transition,
    Arc,
    petrinet_InputArc,
    petrinet_OutputArc,
    Element,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PetriNet,
    petrinet_Element,
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
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"
    assert "minDelay" in params, "Missing parameter 'minDelay'"

def test_petrinet_transition_has_maxDelay():
    assert hasattr(petrinet_Transition, "maxDelay")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_minDelay():
    assert hasattr(petrinet_Transition, "minDelay")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
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
    assert not inspect.isabstract(petrinet_InputArc)


def test_petrinet_inputarc_constructor_exists():
    assert callable(petrinet_InputArc.__init__)


def test_petrinet_inputarc_constructor_args():
    sig = inspect.signature(petrinet_InputArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_outputarc_is_not_abstract():
    assert not inspect.isabstract(petrinet_OutputArc)


def test_petrinet_outputarc_constructor_exists():
    assert callable(petrinet_OutputArc.__init__)


def test_petrinet_outputarc_constructor_args():
    sig = inspect.signature(petrinet_OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(petrinet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(petrinet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(petrinet_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_element_has_name():
    assert hasattr(petrinet_Element, "name")
    descriptor = None
    for klass in petrinet_Element.__mro__:
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
petrinet_Place_strategy = st.builds(
    petrinet_Place,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Arc_strategy = st.builds(
    Arc,
)
petrinet_InputArc_strategy = st.builds(
    petrinet_InputArc,
)
petrinet_OutputArc_strategy = st.builds(
    petrinet_OutputArc,
)
Element_strategy = st.builds(
    Element,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
)
petrinet_Node_strategy = st.builds(
    petrinet_Node,
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
)
petrinet_Element_strategy = st.builds(
    petrinet_Element,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet_InputArc_strategy)
@settings(max_examples=50)
def test_petrinet_inputarc_instantiation(instance):
    assert isinstance(instance, petrinet_InputArc)

@given(instance=petrinet_OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet_outputarc_instantiation(instance):
    assert isinstance(instance, petrinet_OutputArc)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)

@given(instance=petrinet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)

@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)

@given(instance=petrinet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, petrinet_Element)



@given(instance=petrinet_Element_strategy)
def test_petrinet_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
