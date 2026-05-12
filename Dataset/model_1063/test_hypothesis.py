import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    petriNet_Place,
    petriNet_Transition,
    petriNet_Arc,
    petriNet_Node,
    petriNet_PetriNet,
    ArcKind,
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
    assert not inspect.isabstract(petriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinet_place_has_marking():
    assert hasattr(petriNet_Place, "marking")
    descriptor = None
    for klass in petriNet_Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_petrinet_transition_has_max_time():
    assert hasattr(petriNet_Transition, "max_time")
    descriptor = None
    for klass in petriNet_Transition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_min_time():
    assert hasattr(petriNet_Transition, "min_time")
    descriptor = None
    for klass in petriNet_Transition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_petrinet_arc_has_weight():
    assert hasattr(petriNet_Arc, "weight")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_kind():
    assert hasattr(petriNet_Arc, "kind")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petriNet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petriNet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petriNet_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_node_has_name():
    assert hasattr(petriNet_Node, "name")
    descriptor = None
    for klass in petriNet_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(petriNet_PetriNet, "name")
    descriptor = None
    for klass in petriNet_PetriNet.__mro__:
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
Node_strategy = st.builds(
    Node,
)
petriNet_Place_strategy = st.builds(
    petriNet_Place,
    marking=
        st.integers()
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
    max_time=
        st.integers(),
    min_time=
        st.integers()
)
petriNet_Arc_strategy = st.builds(
    petriNet_Arc,
    weight=
        st.integers(),
    kind=
        safe_text
)
petriNet_Node_strategy = st.builds(
    petriNet_Node,
    name=
        safe_text
)
petriNet_PetriNet_strategy = st.builds(
    petriNet_PetriNet,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)



@given(instance=petriNet_Place_strategy)
def test_petrinet_place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)



@given(instance=petriNet_Transition_strategy)
def test_petrinet_transition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original



@given(instance=petriNet_Transition_strategy)
def test_petrinet_transition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=petriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petriNet_Arc)



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=petriNet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petriNet_Node)



@given(instance=petriNet_Node_strategy)
def test_petrinet_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNet)



@given(instance=petriNet_PetriNet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
