import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Edge,
    PetrinetDSL_TPEdge,
    PetrinetDSL_PTEdge,
    Node,
    PetrinetDSL_Transition,
    PetrinetDSL_Place,
    PetrinetDSL_Token,
    Petrinet,
    PetrinetDSL_Edge,
    PetrinetDSL_Node,
    PetrinetDSL_Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_tpedge_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_TPEdge)


def test_petrinetdsl_tpedge_constructor_exists():
    assert callable(PetrinetDSL_TPEdge.__init__)


def test_petrinetdsl_tpedge_constructor_args():
    sig = inspect.signature(PetrinetDSL_TPEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_ptedge_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_PTEdge)


def test_petrinetdsl_ptedge_constructor_exists():
    assert callable(PetrinetDSL_PTEdge.__init__)


def test_petrinetdsl_ptedge_constructor_args():
    sig = inspect.signature(PetrinetDSL_PTEdge.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_transition_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_Transition)


def test_petrinetdsl_transition_constructor_exists():
    assert callable(PetrinetDSL_Transition.__init__)


def test_petrinetdsl_transition_constructor_args():
    sig = inspect.signature(PetrinetDSL_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_place_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_Place)


def test_petrinetdsl_place_constructor_exists():
    assert callable(PetrinetDSL_Place.__init__)


def test_petrinetdsl_place_constructor_args():
    sig = inspect.signature(PetrinetDSL_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_token_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_Token)


def test_petrinetdsl_token_constructor_exists():
    assert callable(PetrinetDSL_Token.__init__)


def test_petrinetdsl_token_constructor_args():
    sig = inspect.signature(PetrinetDSL_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet)


def test_petrinet_constructor_exists():
    assert callable(Petrinet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(Petrinet.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_edge_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_Edge)


def test_petrinetdsl_edge_constructor_exists():
    assert callable(PetrinetDSL_Edge.__init__)


def test_petrinetdsl_edge_constructor_args():
    sig = inspect.signature(PetrinetDSL_Edge.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_node_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_Node)


def test_petrinetdsl_node_constructor_exists():
    assert callable(PetrinetDSL_Node.__init__)


def test_petrinetdsl_node_constructor_args():
    sig = inspect.signature(PetrinetDSL_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL_Petrinet)


def test_petrinetdsl_petrinet_constructor_exists():
    assert callable(PetrinetDSL_Petrinet.__init__)


def test_petrinetdsl_petrinet_constructor_args():
    sig = inspect.signature(PetrinetDSL_Petrinet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_petrinetdsl_petrinet_has_name():
    assert hasattr(PetrinetDSL_Petrinet, "name")
    descriptor = None
    for klass in PetrinetDSL_Petrinet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetdsl_petrinet_has_description():
    assert hasattr(PetrinetDSL_Petrinet, "description")
    descriptor = None
    for klass in PetrinetDSL_Petrinet.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)


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
Edge_strategy = st.builds(
    Edge,
)
PetrinetDSL_TPEdge_strategy = st.builds(
    PetrinetDSL_TPEdge,
)
PetrinetDSL_PTEdge_strategy = st.builds(
    PetrinetDSL_PTEdge,
)
Node_strategy = st.builds(
    Node,
)
PetrinetDSL_Transition_strategy = st.builds(
    PetrinetDSL_Transition,
)
PetrinetDSL_Place_strategy = st.builds(
    PetrinetDSL_Place,
)
PetrinetDSL_Token_strategy = st.builds(
    PetrinetDSL_Token,
)
Petrinet_strategy = st.builds(
    Petrinet,
)
PetrinetDSL_Edge_strategy = st.builds(
    PetrinetDSL_Edge,
)
PetrinetDSL_Node_strategy = st.builds(
    PetrinetDSL_Node,
)
PetrinetDSL_Petrinet_strategy = st.builds(
    PetrinetDSL_Petrinet,
    name=
        safe_text,
    description=
        safe_text
)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=PetrinetDSL_TPEdge_strategy)
@settings(max_examples=50)
def test_petrinetdsl_tpedge_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_TPEdge)

@given(instance=PetrinetDSL_PTEdge_strategy)
@settings(max_examples=50)
def test_petrinetdsl_ptedge_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_PTEdge)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetrinetDSL_Transition_strategy)
@settings(max_examples=50)
def test_petrinetdsl_transition_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_Transition)

@given(instance=PetrinetDSL_Place_strategy)
@settings(max_examples=50)
def test_petrinetdsl_place_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_Place)

@given(instance=PetrinetDSL_Token_strategy)
@settings(max_examples=50)
def test_petrinetdsl_token_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_Token)

@given(instance=Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, Petrinet)

@given(instance=PetrinetDSL_Edge_strategy)
@settings(max_examples=50)
def test_petrinetdsl_edge_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_Edge)

@given(instance=PetrinetDSL_Node_strategy)
@settings(max_examples=50)
def test_petrinetdsl_node_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_Node)

@given(instance=PetrinetDSL_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinetdsl_petrinet_instantiation(instance):
    assert isinstance(instance, PetrinetDSL_Petrinet)



@given(instance=PetrinetDSL_Petrinet_strategy)
def test_petrinetdsl_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetrinetDSL_Petrinet_strategy)
def test_petrinetdsl_petrinet_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
