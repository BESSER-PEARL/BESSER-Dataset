import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    petrinet_Place,
    petrinet_Transition,
    petrinet_Node,
    petrinet_Arc,
    petrinet_Network,
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
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokensCount" in params, "Missing parameter 'tokensCount'"

def test_petrinet_place_has_tokensCount():
    assert hasattr(petrinet_Place, "tokensCount")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "tokensCount" in klass.__dict__:
            descriptor = klass.__dict__["tokensCount"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_node_has_name():
    assert hasattr(petrinet_Node, "name")
    descriptor = None
    for klass in petrinet_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "tokensCount" in params, "Missing parameter 'tokensCount'"

def test_petrinet_arc_has_readOnly():
    assert hasattr(petrinet_Arc, "readOnly")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_kind():
    assert hasattr(petrinet_Arc, "kind")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_tokensCount():
    assert hasattr(petrinet_Arc, "tokensCount")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "tokensCount" in klass.__dict__:
            descriptor = klass.__dict__["tokensCount"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_network_is_not_abstract():
    assert not inspect.isabstract(petrinet_Network)


def test_petrinet_network_constructor_exists():
    assert callable(petrinet_Network.__init__)


def test_petrinet_network_constructor_args():
    sig = inspect.signature(petrinet_Network.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_network_has_name():
    assert hasattr(petrinet_Network, "name")
    descriptor = None
    for klass in petrinet_Network.__mro__:
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
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    tokensCount=
        st.integers()
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Node_strategy = st.builds(
    petrinet_Node,
    name=
        safe_text
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    readOnly=
        st.booleans(),
    kind=
        safe_text,
    tokensCount=
        st.integers()
)
petrinet_Network_strategy = st.builds(
    petrinet_Network,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_tokensCount_setter(instance):
    original = instance.tokensCount
    instance.tokensCount = original
    assert instance.tokensCount == original

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)



@given(instance=petrinet_Node_strategy)
def test_petrinet_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_tokensCount_setter(instance):
    original = instance.tokensCount
    instance.tokensCount = original
    assert instance.tokensCount == original

@given(instance=petrinet_Network_strategy)
@settings(max_examples=50)
def test_petrinet_network_instantiation(instance):
    assert isinstance(instance, petrinet_Network)



@given(instance=petrinet_Network_strategy)
def test_petrinet_network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
