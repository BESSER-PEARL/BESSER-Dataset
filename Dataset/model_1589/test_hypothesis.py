import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    PN_Transition,
    NamedElement,
    PN_Node,
    PN_NamedElement,
    PN_PetriNet,
    Arc,
    PN_InputArc,
    PN_OutputArc,
    PN_Arc,
    PN_Place,
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



def test_pn_transition_is_not_abstract():
    assert not inspect.isabstract(PN_Transition)


def test_pn_transition_constructor_exists():
    assert callable(PN_Transition.__init__)


def test_pn_transition_constructor_args():
    sig = inspect.signature(PN_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"
    assert "minDelay" in params, "Missing parameter 'minDelay'"

def test_pn_transition_has_maxDelay():
    assert hasattr(PN_Transition, "maxDelay")
    descriptor = None
    for klass in PN_Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)

def test_pn_transition_has_minDelay():
    assert hasattr(PN_Transition, "minDelay")
    descriptor = None
    for klass in PN_Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pn_node_is_not_abstract():
    assert not inspect.isabstract(PN_Node)


def test_pn_node_constructor_exists():
    assert callable(PN_Node.__init__)


def test_pn_node_constructor_args():
    sig = inspect.signature(PN_Node.__init__)
    params = list(sig.parameters.keys())



def test_pn_namedelement_is_not_abstract():
    assert not inspect.isabstract(PN_NamedElement)


def test_pn_namedelement_constructor_exists():
    assert callable(PN_NamedElement.__init__)


def test_pn_namedelement_constructor_args():
    sig = inspect.signature(PN_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn_namedelement_has_name():
    assert hasattr(PN_NamedElement, "name")
    descriptor = None
    for klass in PN_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pn_petrinet_is_not_abstract():
    assert not inspect.isabstract(PN_PetriNet)


def test_pn_petrinet_constructor_exists():
    assert callable(PN_PetriNet.__init__)


def test_pn_petrinet_constructor_args():
    sig = inspect.signature(PN_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn_petrinet_has_name():
    assert hasattr(PN_PetriNet, "name")
    descriptor = None
    for klass in PN_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_pn_inputarc_is_not_abstract():
    assert not inspect.isabstract(PN_InputArc)


def test_pn_inputarc_constructor_exists():
    assert callable(PN_InputArc.__init__)


def test_pn_inputarc_constructor_args():
    sig = inspect.signature(PN_InputArc.__init__)
    params = list(sig.parameters.keys())



def test_pn_outputarc_is_not_abstract():
    assert not inspect.isabstract(PN_OutputArc)


def test_pn_outputarc_constructor_exists():
    assert callable(PN_OutputArc.__init__)


def test_pn_outputarc_constructor_args():
    sig = inspect.signature(PN_OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_pn_arc_is_not_abstract():
    assert not inspect.isabstract(PN_Arc)


def test_pn_arc_constructor_exists():
    assert callable(PN_Arc.__init__)


def test_pn_arc_constructor_args():
    sig = inspect.signature(PN_Arc.__init__)
    params = list(sig.parameters.keys())



def test_pn_place_is_not_abstract():
    assert not inspect.isabstract(PN_Place)


def test_pn_place_constructor_exists():
    assert callable(PN_Place.__init__)


def test_pn_place_constructor_args():
    sig = inspect.signature(PN_Place.__init__)
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
Node_strategy = st.builds(
    Node,
)
PN_Transition_strategy = st.builds(
    PN_Transition,
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PN_Node_strategy = st.builds(
    PN_Node,
)
PN_NamedElement_strategy = st.builds(
    PN_NamedElement,
    name=
        safe_text
)
PN_PetriNet_strategy = st.builds(
    PN_PetriNet,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
PN_InputArc_strategy = st.builds(
    PN_InputArc,
)
PN_OutputArc_strategy = st.builds(
    PN_OutputArc,
)
PN_Arc_strategy = st.builds(
    PN_Arc,
)
PN_Place_strategy = st.builds(
    PN_Place,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PN_Transition_strategy)
@settings(max_examples=50)
def test_pn_transition_instantiation(instance):
    assert isinstance(instance, PN_Transition)



@given(instance=PN_Transition_strategy)
def test_pn_transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original



@given(instance=PN_Transition_strategy)
def test_pn_transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=PN_Node_strategy)
@settings(max_examples=50)
def test_pn_node_instantiation(instance):
    assert isinstance(instance, PN_Node)

@given(instance=PN_NamedElement_strategy)
@settings(max_examples=50)
def test_pn_namedelement_instantiation(instance):
    assert isinstance(instance, PN_NamedElement)



@given(instance=PN_NamedElement_strategy)
def test_pn_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PN_PetriNet_strategy)
@settings(max_examples=50)
def test_pn_petrinet_instantiation(instance):
    assert isinstance(instance, PN_PetriNet)



@given(instance=PN_PetriNet_strategy)
def test_pn_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PN_InputArc_strategy)
@settings(max_examples=50)
def test_pn_inputarc_instantiation(instance):
    assert isinstance(instance, PN_InputArc)

@given(instance=PN_OutputArc_strategy)
@settings(max_examples=50)
def test_pn_outputarc_instantiation(instance):
    assert isinstance(instance, PN_OutputArc)

@given(instance=PN_Arc_strategy)
@settings(max_examples=50)
def test_pn_arc_instantiation(instance):
    assert isinstance(instance, PN_Arc)

@given(instance=PN_Place_strategy)
@settings(max_examples=50)
def test_pn_place_instantiation(instance):
    assert isinstance(instance, PN_Place)
