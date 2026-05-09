import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    iritptn::Place,
    iritptn::Transition,
    iritptn::Arc,
    iritptn::Node,
    iritptn::PetriNet,
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



def test_iritptn::place_is_not_abstract():
    assert not inspect.isabstract(iritptn::Place)


def test_iritptn::place_constructor_exists():
    assert callable(iritptn::Place.__init__)


def test_iritptn::place_constructor_args():
    sig = inspect.signature(iritptn::Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_iritptn::place_has_marking():
    assert hasattr(iritptn::Place, "marking")
    descriptor = None
    for klass in iritptn::Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_iritptn::transition_is_not_abstract():
    assert not inspect.isabstract(iritptn::Transition)


def test_iritptn::transition_constructor_exists():
    assert callable(iritptn::Transition.__init__)


def test_iritptn::transition_constructor_args():
    sig = inspect.signature(iritptn::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "tMax" in params, "Missing parameter 'tMax'"

def test_iritptn::transition_has_tMin():
    assert hasattr(iritptn::Transition, "tMin")
    descriptor = None
    for klass in iritptn::Transition.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_iritptn::transition_has_tMax():
    assert hasattr(iritptn::Transition, "tMax")
    descriptor = None
    for klass in iritptn::Transition.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)



def test_iritptn::arc_is_not_abstract():
    assert not inspect.isabstract(iritptn::Arc)


def test_iritptn::arc_constructor_exists():
    assert callable(iritptn::Arc.__init__)


def test_iritptn::arc_constructor_args():
    sig = inspect.signature(iritptn::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_iritptn::arc_has_weight():
    assert hasattr(iritptn::Arc, "weight")
    descriptor = None
    for klass in iritptn::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_iritptn::arc_has_kind():
    assert hasattr(iritptn::Arc, "kind")
    descriptor = None
    for klass in iritptn::Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_iritptn::node_is_not_abstract():
    assert not inspect.isabstract(iritptn::Node)


def test_iritptn::node_constructor_exists():
    assert callable(iritptn::Node.__init__)


def test_iritptn::node_constructor_args():
    sig = inspect.signature(iritptn::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iritptn::node_has_name():
    assert hasattr(iritptn::Node, "name")
    descriptor = None
    for klass in iritptn::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iritptn::petrinet_is_not_abstract():
    assert not inspect.isabstract(iritptn::PetriNet)


def test_iritptn::petrinet_constructor_exists():
    assert callable(iritptn::PetriNet.__init__)


def test_iritptn::petrinet_constructor_args():
    sig = inspect.signature(iritptn::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iritptn::petrinet_has_name():
    assert hasattr(iritptn::PetriNet, "name")
    descriptor = None
    for klass in iritptn::PetriNet.__mro__:
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
        "readArc",
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
iritptn::Place_strategy = st.builds(
    iritptn::Place,
    marking=
        st.integers()
)
iritptn::Transition_strategy = st.builds(
    iritptn::Transition,
    tMin=
        st.integers(),
    tMax=
        st.integers()
)
iritptn::Arc_strategy = st.builds(
    iritptn::Arc,
    weight=
        st.integers(),
    kind=
        safe_text
)
iritptn::Node_strategy = st.builds(
    iritptn::Node,
    name=
        safe_text
)
iritptn::PetriNet_strategy = st.builds(
    iritptn::PetriNet,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=iritptn::Place_strategy)
@settings(max_examples=50)
def test_iritptn::place_instantiation(instance):
    assert isinstance(instance, iritptn::Place)

@given(instance=iritptn::Place_strategy)
def test_iritptn::place_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=iritptn::Place_strategy)
def test_iritptn::place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=iritptn::Transition_strategy)
@settings(max_examples=50)
def test_iritptn::transition_instantiation(instance):
    assert isinstance(instance, iritptn::Transition)

@given(instance=iritptn::Transition_strategy)
def test_iritptn::transition_tMin_type(instance):
    assert isinstance(instance.tMin, int)


@given(instance=iritptn::Transition_strategy)
def test_iritptn::transition_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=iritptn::Transition_strategy)
def test_iritptn::transition_tMax_type(instance):
    assert isinstance(instance.tMax, int)


@given(instance=iritptn::Transition_strategy)
def test_iritptn::transition_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original

@given(instance=iritptn::Arc_strategy)
@settings(max_examples=50)
def test_iritptn::arc_instantiation(instance):
    assert isinstance(instance, iritptn::Arc)

@given(instance=iritptn::Arc_strategy)
def test_iritptn::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=iritptn::Arc_strategy)
def test_iritptn::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=iritptn::Arc_strategy)
def test_iritptn::arc_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=iritptn::Arc_strategy)
def test_iritptn::arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=iritptn::Node_strategy)
@settings(max_examples=50)
def test_iritptn::node_instantiation(instance):
    assert isinstance(instance, iritptn::Node)

@given(instance=iritptn::Node_strategy)
def test_iritptn::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iritptn::Node_strategy)
def test_iritptn::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iritptn::PetriNet_strategy)
@settings(max_examples=50)
def test_iritptn::petrinet_instantiation(instance):
    assert isinstance(instance, iritptn::PetriNet)

@given(instance=iritptn::PetriNet_strategy)
def test_iritptn::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iritptn::PetriNet_strategy)
def test_iritptn::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
