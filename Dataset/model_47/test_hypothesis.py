import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    petrinet_InputArc,
    petrinet_OutputArc,
    Node,
    petrinet_Transition,
    petrinet_Place,
    Element,
    petrinet_Arc,
    petrinet_Node,
    petrinet_Element,
    petrinet_PetriNetRelationship,
    petrinet_PetriNet,
    petrinet_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
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
    assert "name" in params, "Missing parameter 'name'"
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"
    assert "minDelay" in params, "Missing parameter 'minDelay'"

def test_petrinet_node_has_name():
    assert hasattr(petrinet_Node, "name")
    descriptor = None
    for klass in petrinet_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_node_has_maxDelay():
    assert hasattr(petrinet_Node, "maxDelay")
    descriptor = None
    for klass in petrinet_Node.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_node_has_minDelay():
    assert hasattr(petrinet_Node, "minDelay")
    descriptor = None
    for klass in petrinet_Node.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(petrinet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(petrinet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(petrinet_Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinetrelationship_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNetRelationship)


def test_petrinet_petrinetrelationship_constructor_exists():
    assert callable(petrinet_PetriNetRelationship.__init__)


def test_petrinet_petrinetrelationship_constructor_args():
    sig = inspect.signature(petrinet_PetriNetRelationship.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(petrinet_PetriNet, "name")
    descriptor = None
    for klass in petrinet_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_system_is_not_abstract():
    assert not inspect.isabstract(petrinet_System)


def test_petrinet_system_constructor_exists():
    assert callable(petrinet_System.__init__)


def test_petrinet_system_constructor_args():
    sig = inspect.signature(petrinet_System.__init__)
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
Arc_strategy = st.builds(
    Arc,
)
petrinet_InputArc_strategy = st.builds(
    petrinet_InputArc,
)
petrinet_OutputArc_strategy = st.builds(
    petrinet_OutputArc,
)
Node_strategy = st.builds(
    Node,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
)
Element_strategy = st.builds(
    Element,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
)
petrinet_Node_strategy = st.builds(
    petrinet_Node,
    name=
        safe_text,
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
petrinet_Element_strategy = st.builds(
    petrinet_Element,
)
petrinet_PetriNetRelationship_strategy = st.builds(
    petrinet_PetriNetRelationship,
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
    name=
        safe_text
)
petrinet_System_strategy = st.builds(
    petrinet_System,
)

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

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)

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



@given(instance=petrinet_Node_strategy)
def test_petrinet_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinet_Node_strategy)
def test_petrinet_node_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original



@given(instance=petrinet_Node_strategy)
def test_petrinet_node_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=petrinet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, petrinet_Element)

@given(instance=petrinet_PetriNetRelationship_strategy)
@settings(max_examples=50)
def test_petrinet_petrinetrelationship_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNetRelationship)

@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)



@given(instance=petrinet_PetriNet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_System_strategy)
@settings(max_examples=50)
def test_petrinet_system_instantiation(instance):
    assert isinstance(instance, petrinet_System)
