import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNets_Token,
    Node,
    PetriNets_Transition,
    PetriNets_Place,
    PetriNets_Arc,
    PetriNets_Node,
    PetriNets_PetriNet,
    Arc,
    PetriNets_PTArc,
    PetriNets_TPArc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets_token_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Token)


def test_petrinets_token_constructor_exists():
    assert callable(PetriNets_Token.__init__)


def test_petrinets_token_constructor_args():
    sig = inspect.signature(PetriNets_Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Transition)


def test_petrinets_transition_constructor_exists():
    assert callable(PetriNets_Transition.__init__)


def test_petrinets_transition_constructor_args():
    sig = inspect.signature(PetriNets_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Place)


def test_petrinets_place_constructor_exists():
    assert callable(PetriNets_Place.__init__)


def test_petrinets_place_constructor_args():
    sig = inspect.signature(PetriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinets_place_has_tokens():
    assert hasattr(PetriNets_Place, "tokens")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Arc)


def test_petrinets_arc_constructor_exists():
    assert callable(PetriNets_Arc.__init__)


def test_petrinets_arc_constructor_args():
    sig = inspect.signature(PetriNets_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinets_arc_has_weight():
    assert hasattr(PetriNets_Arc, "weight")
    descriptor = None
    for klass in PetriNets_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_node_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Node)


def test_petrinets_node_constructor_exists():
    assert callable(PetriNets_Node.__init__)


def test_petrinets_node_constructor_args():
    sig = inspect.signature(PetriNets_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets_node_has_name():
    assert hasattr(PetriNets_Node, "name")
    descriptor = None
    for klass in PetriNets_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets_PetriNet)


def test_petrinets_petrinet_constructor_exists():
    assert callable(PetriNets_PetriNet.__init__)


def test_petrinets_petrinet_constructor_args():
    sig = inspect.signature(PetriNets_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_petrinets_petrinet_has_bound():
    assert hasattr(PetriNets_PetriNet, "bound")
    descriptor = None
    for klass in PetriNets_PetriNet.__mro__:
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



def test_petrinets_ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNets_PTArc)


def test_petrinets_ptarc_constructor_exists():
    assert callable(PetriNets_PTArc.__init__)


def test_petrinets_ptarc_constructor_args():
    sig = inspect.signature(PetriNets_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNets_TPArc)


def test_petrinets_tparc_constructor_exists():
    assert callable(PetriNets_TPArc.__init__)


def test_petrinets_tparc_constructor_args():
    sig = inspect.signature(PetriNets_TPArc.__init__)
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
PetriNets_Token_strategy = st.builds(
    PetriNets_Token,
)
Node_strategy = st.builds(
    Node,
)
PetriNets_Transition_strategy = st.builds(
    PetriNets_Transition,
)
PetriNets_Place_strategy = st.builds(
    PetriNets_Place,
    tokens=
        st.integers()
)
PetriNets_Arc_strategy = st.builds(
    PetriNets_Arc,
    weight=
        st.integers()
)
PetriNets_Node_strategy = st.builds(
    PetriNets_Node,
    name=
        safe_text
)
PetriNets_PetriNet_strategy = st.builds(
    PetriNets_PetriNet,
    bound=
        st.integers()
)
Arc_strategy = st.builds(
    Arc,
)
PetriNets_PTArc_strategy = st.builds(
    PetriNets_PTArc,
)
PetriNets_TPArc_strategy = st.builds(
    PetriNets_TPArc,
)

@given(instance=PetriNets_Token_strategy)
@settings(max_examples=50)
def test_petrinets_token_instantiation(instance):
    assert isinstance(instance, PetriNets_Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNets_Transition_strategy)
@settings(max_examples=50)
def test_petrinets_transition_instantiation(instance):
    assert isinstance(instance, PetriNets_Transition)

@given(instance=PetriNets_Place_strategy)
@settings(max_examples=50)
def test_petrinets_place_instantiation(instance):
    assert isinstance(instance, PetriNets_Place)



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=PetriNets_Arc_strategy)
@settings(max_examples=50)
def test_petrinets_arc_instantiation(instance):
    assert isinstance(instance, PetriNets_Arc)



@given(instance=PetriNets_Arc_strategy)
def test_petrinets_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNets_Node_strategy)
@settings(max_examples=50)
def test_petrinets_node_instantiation(instance):
    assert isinstance(instance, PetriNets_Node)



@given(instance=PetriNets_Node_strategy)
def test_petrinets_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets_PetriNet)



@given(instance=PetriNets_PetriNet_strategy)
def test_petrinets_petrinet_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNets_PTArc_strategy)
@settings(max_examples=50)
def test_petrinets_ptarc_instantiation(instance):
    assert isinstance(instance, PetriNets_PTArc)

@given(instance=PetriNets_TPArc_strategy)
@settings(max_examples=50)
def test_petrinets_tparc_instantiation(instance):
    assert isinstance(instance, PetriNets_TPArc)
