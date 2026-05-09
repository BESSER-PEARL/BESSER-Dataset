import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    PetriNet::TPArc,
    PetriNet::PTArc,
    Node,
    PetriNet::Transition,
    PetriNet::Place,
    PetriNet::Arc,
    PetriNet::Node,
    PetriNet::PetriNet,
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



def test_petrinet::tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TPArc)


def test_petrinet::tparc_constructor_exists():
    assert callable(PetriNet::TPArc.__init__)


def test_petrinet::tparc_constructor_args():
    sig = inspect.signature(PetriNet::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PTArc)


def test_petrinet::ptarc_constructor_exists():
    assert callable(PetriNet::PTArc.__init__)


def test_petrinet::ptarc_constructor_args():
    sig = inspect.signature(PetriNet::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinet::place_has_marking():
    assert hasattr(PetriNet::Place, "marking")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(PetriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(PetriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_name():
    assert hasattr(PetriNet::Arc, "name")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_weight():
    assert hasattr(PetriNet::Arc, "weight")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(PetriNet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(PetriNet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::node_has_name():
    assert hasattr(PetriNet::Node, "name")
    descriptor = None
    for klass in PetriNet::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(PetriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(PetriNet::PetriNet.__init__)
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
PetriNet::TPArc_strategy = st.builds(
    PetriNet::TPArc,
)
PetriNet::PTArc_strategy = st.builds(
    PetriNet::PTArc,
)
Node_strategy = st.builds(
    Node,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    marking=
        st.integers()
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    name=
        safe_text,
    weight=
        st.integers()
)
PetriNet::Node_strategy = st.builds(
    PetriNet::Node,
    name=
        safe_text
)
PetriNet::PetriNet_strategy = st.builds(
    PetriNet::PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet::TPArc_strategy)
@settings(max_examples=50)
def test_petrinet::tparc_instantiation(instance):
    assert isinstance(instance, PetriNet::TPArc)

@given(instance=PetriNet::PTArc_strategy)
@settings(max_examples=50)
def test_petrinet::ptarc_instantiation(instance):
    assert isinstance(instance, PetriNet::PTArc)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, PetriNet::Node)

@given(instance=PetriNet::Node_strategy)
def test_petrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Node_strategy)
def test_petrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNet)
