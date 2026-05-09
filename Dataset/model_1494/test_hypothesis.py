import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    PetriNets::Transition,
    PetriNets::Place,
    PetriNets::Arc,
    PetriNets::Node,
    PetriNets::PetriNet,
    Arc,
    PetriNets::PTArc,
    PetriNets::TPArc,
    PetriNets::Token,
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



def test_petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Transition)


def test_petrinets::transition_constructor_exists():
    assert callable(PetriNets::Transition.__init__)


def test_petrinets::transition_constructor_args():
    sig = inspect.signature(PetriNets::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::place_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Place)


def test_petrinets::place_constructor_exists():
    assert callable(PetriNets::Place.__init__)


def test_petrinets::place_constructor_args():
    sig = inspect.signature(PetriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinets::place_has_tokens():
    assert hasattr(PetriNets::Place, "tokens")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Arc)


def test_petrinets::arc_constructor_exists():
    assert callable(PetriNets::Arc.__init__)


def test_petrinets::arc_constructor_args():
    sig = inspect.signature(PetriNets::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinets::arc_has_weight():
    assert hasattr(PetriNets::Arc, "weight")
    descriptor = None
    for klass in PetriNets::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::node_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Node)


def test_petrinets::node_constructor_exists():
    assert callable(PetriNets::Node.__init__)


def test_petrinets::node_constructor_args():
    sig = inspect.signature(PetriNets::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets::node_has_name():
    assert hasattr(PetriNets::Node, "name")
    descriptor = None
    for klass in PetriNets::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets::PetriNet)


def test_petrinets::petrinet_constructor_exists():
    assert callable(PetriNets::PetriNet.__init__)


def test_petrinets::petrinet_constructor_args():
    sig = inspect.signature(PetriNets::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_petrinets::petrinet_has_bound():
    assert hasattr(PetriNets::PetriNet, "bound")
    descriptor = None
    for klass in PetriNets::PetriNet.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNets::PTArc)


def test_petrinets::ptarc_constructor_exists():
    assert callable(PetriNets::PTArc.__init__)


def test_petrinets::ptarc_constructor_args():
    sig = inspect.signature(PetriNets::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNets::TPArc)


def test_petrinets::tparc_constructor_exists():
    assert callable(PetriNets::TPArc.__init__)


def test_petrinets::tparc_constructor_args():
    sig = inspect.signature(PetriNets::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::token_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Token)


def test_petrinets::token_constructor_exists():
    assert callable(PetriNets::Token.__init__)


def test_petrinets::token_constructor_args():
    sig = inspect.signature(PetriNets::Token.__init__)
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
Node_strategy = st.builds(
    Node,
)
PetriNets::Transition_strategy = st.builds(
    PetriNets::Transition,
)
PetriNets::Place_strategy = st.builds(
    PetriNets::Place,
    tokens=
        st.integers()
)
PetriNets::Arc_strategy = st.builds(
    PetriNets::Arc,
    weight=
        st.integers()
)
PetriNets::Node_strategy = st.builds(
    PetriNets::Node,
    name=
        safe_text
)
PetriNets::PetriNet_strategy = st.builds(
    PetriNets::PetriNet,
    bound=
        st.integers()
)
Arc_strategy = st.builds(
    Arc,
)
PetriNets::PTArc_strategy = st.builds(
    PetriNets::PTArc,
)
PetriNets::TPArc_strategy = st.builds(
    PetriNets::TPArc,
)
PetriNets::Token_strategy = st.builds(
    PetriNets::Token,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNets::Transition_strategy)
@settings(max_examples=50)
def test_petrinets::transition_instantiation(instance):
    assert isinstance(instance, PetriNets::Transition)

@given(instance=PetriNets::Place_strategy)
@settings(max_examples=50)
def test_petrinets::place_instantiation(instance):
    assert isinstance(instance, PetriNets::Place)

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=PetriNets::Arc_strategy)
@settings(max_examples=50)
def test_petrinets::arc_instantiation(instance):
    assert isinstance(instance, PetriNets::Arc)

@given(instance=PetriNets::Arc_strategy)
def test_petrinets::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNets::Arc_strategy)
def test_petrinets::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNets::Node_strategy)
@settings(max_examples=50)
def test_petrinets::node_instantiation(instance):
    assert isinstance(instance, PetriNets::Node)

@given(instance=PetriNets::Node_strategy)
def test_petrinets::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNets::Node_strategy)
def test_petrinets::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets::PetriNet)

@given(instance=PetriNets::PetriNet_strategy)
def test_petrinets::petrinet_bound_type(instance):
    assert isinstance(instance.bound, int)


@given(instance=PetriNets::PetriNet_strategy)
def test_petrinets::petrinet_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNets::PTArc_strategy)
@settings(max_examples=50)
def test_petrinets::ptarc_instantiation(instance):
    assert isinstance(instance, PetriNets::PTArc)

@given(instance=PetriNets::TPArc_strategy)
@settings(max_examples=50)
def test_petrinets::tparc_instantiation(instance):
    assert isinstance(instance, PetriNets::TPArc)

@given(instance=PetriNets::Token_strategy)
@settings(max_examples=50)
def test_petrinets::token_instantiation(instance):
    assert isinstance(instance, PetriNets::Token)
