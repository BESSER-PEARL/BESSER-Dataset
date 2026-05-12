import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    PetriNet_Place,
    PetriNet_Transition,
    PetriNet_Arc,
    PetriNet_Node,
    PetriNet_PetriNet,
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



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_petrinet_transition_has_max_time():
    assert hasattr(PetriNet_Transition, "max_time")
    descriptor = None
    for klass in PetriNet_Transition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_min_time():
    assert hasattr(PetriNet_Transition, "min_time")
    descriptor = None
    for klass in PetriNet_Transition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_arc_has_kind():
    assert hasattr(PetriNet_Arc, "kind")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
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
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(PetriNet_PetriNet, "name")
    descriptor = None
    for klass in PetriNet_PetriNet.__mro__:
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
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    marking=
        st.integers()
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
    max_time=
        st.integers(),
    min_time=
        st.integers()
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    kind=
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
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)



@given(instance=PetriNet_Transition_strategy)
def test_petrinet_transition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original



@given(instance=PetriNet_Transition_strategy)
def test_petrinet_transition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



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



@given(instance=PetriNet_PetriNet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
