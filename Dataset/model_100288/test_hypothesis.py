import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petriNet::Arc,
    petriNet::Node,
    Node,
    petriNet::Place,
    petriNet::Transition,
    petriNet::PetriNet,
    ArcKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_petrinet::arc_has_weight():
    assert hasattr(petriNet::Arc, "weight")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_kind():
    assert hasattr(petriNet::Arc, "kind")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petriNet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petriNet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petriNet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::node_has_name():
    assert hasattr(petriNet::Node, "name")
    descriptor = None
    for klass in petriNet::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinet::place_has_marking():
    assert hasattr(petriNet::Place, "marking")
    descriptor = None
    for klass in petriNet::Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petriNet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "min_time" in params, "Missing parameter 'min_time'"
    assert "max_time" in params, "Missing parameter 'max_time'"

def test_petrinet::transition_has_min_time():
    assert hasattr(petriNet::Transition, "min_time")
    descriptor = None
    for klass in petriNet::Transition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::transition_has_max_time():
    assert hasattr(petriNet::Transition, "max_time")
    descriptor = None
    for klass in petriNet::Transition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petriNet::PetriNet, "name")
    descriptor = None
    for klass in petriNet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arckind_exists():
    # Check that the Enumeration exists
    assert ArcKind is not None

def test_arckind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcKind]
    expected_literals = [
        "normal",
        "read_arc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcKind"


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
petriNet::Arc_strategy = st.builds(
    petriNet::Arc,
    weight=
        st.integers(),
    kind=
        safe_text
)
petriNet::Node_strategy = st.builds(
    petriNet::Node,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
petriNet::Place_strategy = st.builds(
    petriNet::Place,
    marking=
        st.integers()
)
petriNet::Transition_strategy = st.builds(
    petriNet::Transition,
    min_time=
        st.integers(),
    max_time=
        st.integers()
)
petriNet::PetriNet_strategy = st.builds(
    petriNet::PetriNet,
    name=
        safe_text
)

@given(instance=petriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petriNet::Arc)

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=petriNet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petriNet::Node)

@given(instance=petriNet::Node_strategy)
def test_petrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::Node_strategy)
def test_petrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petriNet::Place)

@given(instance=petriNet::Place_strategy)
def test_petrinet::place_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=petriNet::Place_strategy)
def test_petrinet::place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petriNet::Transition)

@given(instance=petriNet::Transition_strategy)
def test_petrinet::transition_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=petriNet::Transition_strategy)
def test_petrinet::transition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=petriNet::Transition_strategy)
def test_petrinet::transition_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=petriNet::Transition_strategy)
def test_petrinet::transition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=petriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNet)

@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
