import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    iritptn_Place,
    iritptn_Transition,
    iritptn_Arc,
    iritptn_Node,
    iritptn_PetriNet,
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



def test_iritptn_place_is_not_abstract():
    assert not inspect.isabstract(iritptn_Place)


def test_iritptn_place_constructor_exists():
    assert callable(iritptn_Place.__init__)


def test_iritptn_place_constructor_args():
    sig = inspect.signature(iritptn_Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_iritptn_place_has_marking():
    assert hasattr(iritptn_Place, "marking")
    descriptor = None
    for klass in iritptn_Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_iritptn_transition_is_not_abstract():
    assert not inspect.isabstract(iritptn_Transition)


def test_iritptn_transition_constructor_exists():
    assert callable(iritptn_Transition.__init__)


def test_iritptn_transition_constructor_args():
    sig = inspect.signature(iritptn_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "tMax" in params, "Missing parameter 'tMax'"

def test_iritptn_transition_has_tMin():
    assert hasattr(iritptn_Transition, "tMin")
    descriptor = None
    for klass in iritptn_Transition.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_iritptn_transition_has_tMax():
    assert hasattr(iritptn_Transition, "tMax")
    descriptor = None
    for klass in iritptn_Transition.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)



def test_iritptn_arc_is_not_abstract():
    assert not inspect.isabstract(iritptn_Arc)


def test_iritptn_arc_constructor_exists():
    assert callable(iritptn_Arc.__init__)


def test_iritptn_arc_constructor_args():
    sig = inspect.signature(iritptn_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_iritptn_arc_has_weight():
    assert hasattr(iritptn_Arc, "weight")
    descriptor = None
    for klass in iritptn_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_iritptn_arc_has_kind():
    assert hasattr(iritptn_Arc, "kind")
    descriptor = None
    for klass in iritptn_Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_iritptn_node_is_not_abstract():
    assert not inspect.isabstract(iritptn_Node)


def test_iritptn_node_constructor_exists():
    assert callable(iritptn_Node.__init__)


def test_iritptn_node_constructor_args():
    sig = inspect.signature(iritptn_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iritptn_node_has_name():
    assert hasattr(iritptn_Node, "name")
    descriptor = None
    for klass in iritptn_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iritptn_petrinet_is_not_abstract():
    assert not inspect.isabstract(iritptn_PetriNet)


def test_iritptn_petrinet_constructor_exists():
    assert callable(iritptn_PetriNet.__init__)


def test_iritptn_petrinet_constructor_args():
    sig = inspect.signature(iritptn_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iritptn_petrinet_has_name():
    assert hasattr(iritptn_PetriNet, "name")
    descriptor = None
    for klass in iritptn_PetriNet.__mro__:
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
        "readArc",
        "normal",
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
iritptn_Place_strategy = st.builds(
    iritptn_Place,
    marking=
        st.integers()
)
iritptn_Transition_strategy = st.builds(
    iritptn_Transition,
    tMin=
        st.integers(),
    tMax=
        st.integers()
)
iritptn_Arc_strategy = st.builds(
    iritptn_Arc,
    weight=
        st.integers(),
    kind=
        safe_text
)
iritptn_Node_strategy = st.builds(
    iritptn_Node,
    name=
        safe_text
)
iritptn_PetriNet_strategy = st.builds(
    iritptn_PetriNet,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=iritptn_Place_strategy)
@settings(max_examples=50)
def test_iritptn_place_instantiation(instance):
    assert isinstance(instance, iritptn_Place)



@given(instance=iritptn_Place_strategy)
def test_iritptn_place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=iritptn_Transition_strategy)
@settings(max_examples=50)
def test_iritptn_transition_instantiation(instance):
    assert isinstance(instance, iritptn_Transition)



@given(instance=iritptn_Transition_strategy)
def test_iritptn_transition_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original



@given(instance=iritptn_Transition_strategy)
def test_iritptn_transition_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original

@given(instance=iritptn_Arc_strategy)
@settings(max_examples=50)
def test_iritptn_arc_instantiation(instance):
    assert isinstance(instance, iritptn_Arc)



@given(instance=iritptn_Arc_strategy)
def test_iritptn_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=iritptn_Arc_strategy)
def test_iritptn_arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=iritptn_Node_strategy)
@settings(max_examples=50)
def test_iritptn_node_instantiation(instance):
    assert isinstance(instance, iritptn_Node)



@given(instance=iritptn_Node_strategy)
def test_iritptn_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iritptn_PetriNet_strategy)
@settings(max_examples=50)
def test_iritptn_petrinet_instantiation(instance):
    assert isinstance(instance, iritptn_PetriNet)



@given(instance=iritptn_PetriNet_strategy)
def test_iritptn_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
