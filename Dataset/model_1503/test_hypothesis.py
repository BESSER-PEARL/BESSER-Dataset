import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    petri_PTArc,
    petri_TPArc,
    Node,
    petri_Transition,
    petri_Place,
    petri_Arc,
    petri_Node,
    petri_PetriNet,
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



def test_petri_ptarc_is_not_abstract():
    assert not inspect.isabstract(petri_PTArc)


def test_petri_ptarc_constructor_exists():
    assert callable(petri_PTArc.__init__)


def test_petri_ptarc_constructor_args():
    sig = inspect.signature(petri_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petri_tparc_is_not_abstract():
    assert not inspect.isabstract(petri_TPArc)


def test_petri_tparc_constructor_exists():
    assert callable(petri_TPArc.__init__)


def test_petri_tparc_constructor_args():
    sig = inspect.signature(petri_TPArc.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petri_transition_is_not_abstract():
    assert not inspect.isabstract(petri_Transition)


def test_petri_transition_constructor_exists():
    assert callable(petri_Transition.__init__)


def test_petri_transition_constructor_args():
    sig = inspect.signature(petri_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri_place_is_not_abstract():
    assert not inspect.isabstract(petri_Place)


def test_petri_place_constructor_exists():
    assert callable(petri_Place.__init__)


def test_petri_place_constructor_args():
    sig = inspect.signature(petri_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petri_place_has_tokens():
    assert hasattr(petri_Place, "tokens")
    descriptor = None
    for klass in petri_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petri_arc_is_not_abstract():
    assert not inspect.isabstract(petri_Arc)


def test_petri_arc_constructor_exists():
    assert callable(petri_Arc.__init__)


def test_petri_arc_constructor_args():
    sig = inspect.signature(petri_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petri_node_is_not_abstract():
    assert not inspect.isabstract(petri_Node)


def test_petri_node_constructor_exists():
    assert callable(petri_Node.__init__)


def test_petri_node_constructor_args():
    sig = inspect.signature(petri_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_node_has_name():
    assert hasattr(petri_Node, "name")
    descriptor = None
    for klass in petri_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri_petrinet_is_not_abstract():
    assert not inspect.isabstract(petri_PetriNet)


def test_petri_petrinet_constructor_exists():
    assert callable(petri_PetriNet.__init__)


def test_petri_petrinet_constructor_args():
    sig = inspect.signature(petri_PetriNet.__init__)
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
petri_PTArc_strategy = st.builds(
    petri_PTArc,
)
petri_TPArc_strategy = st.builds(
    petri_TPArc,
)
Node_strategy = st.builds(
    Node,
)
petri_Transition_strategy = st.builds(
    petri_Transition,
)
petri_Place_strategy = st.builds(
    petri_Place,
    tokens=
        st.integers()
)
petri_Arc_strategy = st.builds(
    petri_Arc,
)
petri_Node_strategy = st.builds(
    petri_Node,
    name=
        safe_text
)
petri_PetriNet_strategy = st.builds(
    petri_PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petri_PTArc_strategy)
@settings(max_examples=50)
def test_petri_ptarc_instantiation(instance):
    assert isinstance(instance, petri_PTArc)

@given(instance=petri_TPArc_strategy)
@settings(max_examples=50)
def test_petri_tparc_instantiation(instance):
    assert isinstance(instance, petri_TPArc)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petri_Transition_strategy)
@settings(max_examples=50)
def test_petri_transition_instantiation(instance):
    assert isinstance(instance, petri_Transition)

@given(instance=petri_Place_strategy)
@settings(max_examples=50)
def test_petri_place_instantiation(instance):
    assert isinstance(instance, petri_Place)



@given(instance=petri_Place_strategy)
def test_petri_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=petri_Arc_strategy)
@settings(max_examples=50)
def test_petri_arc_instantiation(instance):
    assert isinstance(instance, petri_Arc)

@given(instance=petri_Node_strategy)
@settings(max_examples=50)
def test_petri_node_instantiation(instance):
    assert isinstance(instance, petri_Node)



@given(instance=petri_Node_strategy)
def test_petri_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri_PetriNet_strategy)
@settings(max_examples=50)
def test_petri_petrinet_instantiation(instance):
    assert isinstance(instance, petri_PetriNet)
