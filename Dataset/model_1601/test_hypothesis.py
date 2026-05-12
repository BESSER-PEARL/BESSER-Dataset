import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stochasticpetrinet_Arc,
    Node,
    stochasticpetrinet_Place,
    stochasticpetrinet_Transition,
    stochasticpetrinet_Node,
    stochasticpetrinet_PetriNet,
    Transition,
    stochasticpetrinet_ImmediateTransition,
    stochasticpetrinet_TimedTransition,
    ArcKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stochasticpetrinet_arc_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_Arc)


def test_stochasticpetrinet_arc_constructor_exists():
    assert callable(stochasticpetrinet_Arc.__init__)


def test_stochasticpetrinet_arc_constructor_args():
    sig = inspect.signature(stochasticpetrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_stochasticpetrinet_arc_has_kind():
    assert hasattr(stochasticpetrinet_Arc, "kind")
    descriptor = None
    for klass in stochasticpetrinet_Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet_place_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_Place)


def test_stochasticpetrinet_place_constructor_exists():
    assert callable(stochasticpetrinet_Place.__init__)


def test_stochasticpetrinet_place_constructor_args():
    sig = inspect.signature(stochasticpetrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_stochasticpetrinet_place_has_tokens():
    assert hasattr(stochasticpetrinet_Place, "tokens")
    descriptor = None
    for klass in stochasticpetrinet_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_stochasticpetrinet_transition_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_Transition)


def test_stochasticpetrinet_transition_constructor_exists():
    assert callable(stochasticpetrinet_Transition.__init__)


def test_stochasticpetrinet_transition_constructor_args():
    sig = inspect.signature(stochasticpetrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet_node_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_Node)


def test_stochasticpetrinet_node_constructor_exists():
    assert callable(stochasticpetrinet_Node.__init__)


def test_stochasticpetrinet_node_constructor_args():
    sig = inspect.signature(stochasticpetrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_PetriNet)


def test_stochasticpetrinet_petrinet_constructor_exists():
    assert callable(stochasticpetrinet_PetriNet.__init__)


def test_stochasticpetrinet_petrinet_constructor_args():
    sig = inspect.signature(stochasticpetrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet_immediatetransition_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_ImmediateTransition)


def test_stochasticpetrinet_immediatetransition_constructor_exists():
    assert callable(stochasticpetrinet_ImmediateTransition.__init__)


def test_stochasticpetrinet_immediatetransition_constructor_args():
    sig = inspect.signature(stochasticpetrinet_ImmediateTransition.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet_timedtransition_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet_TimedTransition)


def test_stochasticpetrinet_timedtransition_constructor_exists():
    assert callable(stochasticpetrinet_TimedTransition.__init__)


def test_stochasticpetrinet_timedtransition_constructor_args():
    sig = inspect.signature(stochasticpetrinet_TimedTransition.__init__)
    params = list(sig.parameters.keys())

def test_arckind_exists():
    # Check that the Enumeration exists
    assert ArcKind is not None

def test_arckind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcKind]
    expected_literals = [
        "OUTPUT",
        "INPUT",
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
stochasticpetrinet_Arc_strategy = st.builds(
    stochasticpetrinet_Arc,
    kind=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
stochasticpetrinet_Place_strategy = st.builds(
    stochasticpetrinet_Place,
    tokens=
        st.integers()
)
stochasticpetrinet_Transition_strategy = st.builds(
    stochasticpetrinet_Transition,
)
stochasticpetrinet_Node_strategy = st.builds(
    stochasticpetrinet_Node,
)
stochasticpetrinet_PetriNet_strategy = st.builds(
    stochasticpetrinet_PetriNet,
)
Transition_strategy = st.builds(
    Transition,
)
stochasticpetrinet_ImmediateTransition_strategy = st.builds(
    stochasticpetrinet_ImmediateTransition,
)
stochasticpetrinet_TimedTransition_strategy = st.builds(
    stochasticpetrinet_TimedTransition,
)

@given(instance=stochasticpetrinet_Arc_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_arc_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_Arc)



@given(instance=stochasticpetrinet_Arc_strategy)
def test_stochasticpetrinet_arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=stochasticpetrinet_Place_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_place_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_Place)



@given(instance=stochasticpetrinet_Place_strategy)
def test_stochasticpetrinet_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=stochasticpetrinet_Transition_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_transition_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_Transition)

@given(instance=stochasticpetrinet_Node_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_node_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_Node)

@given(instance=stochasticpetrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_petrinet_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_PetriNet)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=stochasticpetrinet_ImmediateTransition_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_immediatetransition_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_ImmediateTransition)

@given(instance=stochasticpetrinet_TimedTransition_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet_timedtransition_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet_TimedTransition)
