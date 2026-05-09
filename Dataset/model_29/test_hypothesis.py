import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    petrinet::Place,
    petrinet::Transition,
    petrinet::Arc,
    petrinet::Node,
    petrinet::Network,
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



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokensCount" in params, "Missing parameter 'tokensCount'"

def test_petrinet::place_has_tokensCount():
    assert hasattr(petrinet::Place, "tokensCount")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "tokensCount" in klass.__dict__:
            descriptor = klass.__dict__["tokensCount"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "tokensCount" in params, "Missing parameter 'tokensCount'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_petrinet::arc_has_kind():
    assert hasattr(petrinet::Arc, "kind")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_tokensCount():
    assert hasattr(petrinet::Arc, "tokensCount")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "tokensCount" in klass.__dict__:
            descriptor = klass.__dict__["tokensCount"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_readOnly():
    assert hasattr(petrinet::Arc, "readOnly")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::node_has_name():
    assert hasattr(petrinet::Node, "name")
    descriptor = None
    for klass in petrinet::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::network_is_not_abstract():
    assert not inspect.isabstract(petrinet::Network)


def test_petrinet::network_constructor_exists():
    assert callable(petrinet::Network.__init__)


def test_petrinet::network_constructor_args():
    sig = inspect.signature(petrinet::Network.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::network_has_name():
    assert hasattr(petrinet::Network, "name")
    descriptor = None
    for klass in petrinet::Network.__mro__:
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
        "read_arc",
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
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    tokensCount=
        st.integers()
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    kind=
        safe_text,
    tokensCount=
        st.integers(),
    readOnly=
        st.booleans()
)
petrinet::Node_strategy = st.builds(
    petrinet::Node,
    name=
        safe_text
)
petrinet::Network_strategy = st.builds(
    petrinet::Network,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_tokensCount_type(instance):
    assert isinstance(instance.tokensCount, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_tokensCount_setter(instance):
    original = instance.tokensCount
    instance.tokensCount = original
    assert instance.tokensCount == original

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_tokensCount_type(instance):
    assert isinstance(instance.tokensCount, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_tokensCount_setter(instance):
    original = instance.tokensCount
    instance.tokensCount = original
    assert instance.tokensCount == original

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Network_strategy)
@settings(max_examples=50)
def test_petrinet::network_instantiation(instance):
    assert isinstance(instance, petrinet::Network)

@given(instance=petrinet::Network_strategy)
def test_petrinet::network_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Network_strategy)
def test_petrinet::network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
