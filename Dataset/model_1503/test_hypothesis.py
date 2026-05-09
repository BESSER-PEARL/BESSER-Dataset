import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    petri::PTArc,
    petri::TPArc,
    Node,
    petri::Transition,
    petri::Place,
    petri::Arc,
    petri::Node,
    petri::PetriNet,
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



def test_petri::ptarc_is_not_abstract():
    assert not inspect.isabstract(petri::PTArc)


def test_petri::ptarc_constructor_exists():
    assert callable(petri::PTArc.__init__)


def test_petri::ptarc_constructor_args():
    sig = inspect.signature(petri::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petri::tparc_is_not_abstract():
    assert not inspect.isabstract(petri::TPArc)


def test_petri::tparc_constructor_exists():
    assert callable(petri::TPArc.__init__)


def test_petri::tparc_constructor_args():
    sig = inspect.signature(petri::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petri::transition_is_not_abstract():
    assert not inspect.isabstract(petri::Transition)


def test_petri::transition_constructor_exists():
    assert callable(petri::Transition.__init__)


def test_petri::transition_constructor_args():
    sig = inspect.signature(petri::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri::place_is_not_abstract():
    assert not inspect.isabstract(petri::Place)


def test_petri::place_constructor_exists():
    assert callable(petri::Place.__init__)


def test_petri::place_constructor_args():
    sig = inspect.signature(petri::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petri::place_has_tokens():
    assert hasattr(petri::Place, "tokens")
    descriptor = None
    for klass in petri::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petri::arc_is_not_abstract():
    assert not inspect.isabstract(petri::Arc)


def test_petri::arc_constructor_exists():
    assert callable(petri::Arc.__init__)


def test_petri::arc_constructor_args():
    sig = inspect.signature(petri::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petri::node_is_not_abstract():
    assert not inspect.isabstract(petri::Node)


def test_petri::node_constructor_exists():
    assert callable(petri::Node.__init__)


def test_petri::node_constructor_args():
    sig = inspect.signature(petri::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::node_has_name():
    assert hasattr(petri::Node, "name")
    descriptor = None
    for klass in petri::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri::petrinet_is_not_abstract():
    assert not inspect.isabstract(petri::PetriNet)


def test_petri::petrinet_constructor_exists():
    assert callable(petri::PetriNet.__init__)


def test_petri::petrinet_constructor_args():
    sig = inspect.signature(petri::PetriNet.__init__)
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
petri::PTArc_strategy = st.builds(
    petri::PTArc,
)
petri::TPArc_strategy = st.builds(
    petri::TPArc,
)
Node_strategy = st.builds(
    Node,
)
petri::Transition_strategy = st.builds(
    petri::Transition,
)
petri::Place_strategy = st.builds(
    petri::Place,
    tokens=
        st.integers()
)
petri::Arc_strategy = st.builds(
    petri::Arc,
)
petri::Node_strategy = st.builds(
    petri::Node,
    name=
        safe_text
)
petri::PetriNet_strategy = st.builds(
    petri::PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petri::PTArc_strategy)
@settings(max_examples=50)
def test_petri::ptarc_instantiation(instance):
    assert isinstance(instance, petri::PTArc)

@given(instance=petri::TPArc_strategy)
@settings(max_examples=50)
def test_petri::tparc_instantiation(instance):
    assert isinstance(instance, petri::TPArc)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petri::Transition_strategy)
@settings(max_examples=50)
def test_petri::transition_instantiation(instance):
    assert isinstance(instance, petri::Transition)

@given(instance=petri::Place_strategy)
@settings(max_examples=50)
def test_petri::place_instantiation(instance):
    assert isinstance(instance, petri::Place)

@given(instance=petri::Place_strategy)
def test_petri::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=petri::Place_strategy)
def test_petri::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=petri::Arc_strategy)
@settings(max_examples=50)
def test_petri::arc_instantiation(instance):
    assert isinstance(instance, petri::Arc)

@given(instance=petri::Node_strategy)
@settings(max_examples=50)
def test_petri::node_instantiation(instance):
    assert isinstance(instance, petri::Node)

@given(instance=petri::Node_strategy)
def test_petri::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::Node_strategy)
def test_petri::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri::PetriNet_strategy)
@settings(max_examples=50)
def test_petri::petrinet_instantiation(instance):
    assert isinstance(instance, petri::PetriNet)
