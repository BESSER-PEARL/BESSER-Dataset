import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    PetriNet_TPArc,
    PetriNet_PTArc,
    Node,
    PetriNet_Transition,
    PetriNet_Place,
    PetriNet_Arc,
    PetriNet_Node,
    PetriNet_PetriNet,
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



def test_petrinet_tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_TPArc)


def test_petrinet_tparc_constructor_exists():
    assert callable(PetriNet_TPArc.__init__)


def test_petrinet_tparc_constructor_args():
    sig = inspect.signature(PetriNet_TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PTArc)


def test_petrinet_ptarc_constructor_exists():
    assert callable(PetriNet_PTArc.__init__)


def test_petrinet_ptarc_constructor_args():
    sig = inspect.signature(PetriNet_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinet_place_has_marking():
    assert hasattr(PetriNet_Place, "marking")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_arc_has_name():
    assert hasattr(PetriNet_Arc, "name")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_weight():
    assert hasattr(PetriNet_Arc, "weight")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(PetriNet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(PetriNet_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_node_has_name():
    assert hasattr(PetriNet_Node, "name")
    descriptor = None
    for klass in PetriNet_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(PetriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(PetriNet_PetriNet.__init__)
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
PetriNet_TPArc_strategy = st.builds(
    PetriNet_TPArc,
)
PetriNet_PTArc_strategy = st.builds(
    PetriNet_PTArc,
)
Node_strategy = st.builds(
    Node,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    marking=
        st.integers()
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    name=
        safe_text,
    weight=
        st.integers()
)
PetriNet_Node_strategy = st.builds(
    PetriNet_Node,
    name=
        safe_text
)
PetriNet_PetriNet_strategy = st.builds(
    PetriNet_PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet_TPArc_strategy)
@settings(max_examples=50)
def test_petrinet_tparc_instantiation(instance):
    assert isinstance(instance, PetriNet_TPArc)

@given(instance=PetriNet_PTArc_strategy)
@settings(max_examples=50)
def test_petrinet_ptarc_instantiation(instance):
    assert isinstance(instance, PetriNet_PTArc)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, PetriNet_Node)



@given(instance=PetriNet_Node_strategy)
def test_petrinet_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNet)
