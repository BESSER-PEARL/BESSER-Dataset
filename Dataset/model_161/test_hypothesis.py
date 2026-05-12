import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PObject,
    PetriNetModel_Arc,
    PetriNetModel_Node,
    PetriNetModel_PObject,
    PetriNetModel_PetriNet,
    PetriNetModel_Token,
    Node,
    PetriNetModel_Place,
    PetriNetModel_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pobject_is_not_abstract():
    assert not inspect.isabstract(PObject)


def test_pobject_constructor_exists():
    assert callable(PObject.__init__)


def test_pobject_constructor_args():
    sig = inspect.signature(PObject.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Arc)


def test_petrinetmodel_arc_constructor_exists():
    assert callable(PetriNetModel_Arc.__init__)


def test_petrinetmodel_arc_constructor_args():
    sig = inspect.signature(PetriNetModel_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel_node_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Node)


def test_petrinetmodel_node_constructor_exists():
    assert callable(PetriNetModel_Node.__init__)


def test_petrinetmodel_node_constructor_args():
    sig = inspect.signature(PetriNetModel_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmodel_node_has_name():
    assert hasattr(PetriNetModel_Node, "name")
    descriptor = None
    for klass in PetriNetModel_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_pobject_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_PObject)


def test_petrinetmodel_pobject_constructor_exists():
    assert callable(PetriNetModel_PObject.__init__)


def test_petrinetmodel_pobject_constructor_args():
    sig = inspect.signature(PetriNetModel_PObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_petrinetmodel_pobject_has_id():
    assert hasattr(PetriNetModel_PObject, "id")
    descriptor = None
    for klass in PetriNetModel_PObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_PetriNet)


def test_petrinetmodel_petrinet_constructor_exists():
    assert callable(PetriNetModel_PetriNet.__init__)


def test_petrinetmodel_petrinet_constructor_args():
    sig = inspect.signature(PetriNetModel_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel_token_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Token)


def test_petrinetmodel_token_constructor_exists():
    assert callable(PetriNetModel_Token.__init__)


def test_petrinetmodel_token_constructor_args():
    sig = inspect.signature(PetriNetModel_Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel_place_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Place)


def test_petrinetmodel_place_constructor_exists():
    assert callable(PetriNetModel_Place.__init__)


def test_petrinetmodel_place_constructor_args():
    sig = inspect.signature(PetriNetModel_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Transition)


def test_petrinetmodel_transition_constructor_exists():
    assert callable(PetriNetModel_Transition.__init__)


def test_petrinetmodel_transition_constructor_args():
    sig = inspect.signature(PetriNetModel_Transition.__init__)
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
PObject_strategy = st.builds(
    PObject,
)
PetriNetModel_Arc_strategy = st.builds(
    PetriNetModel_Arc,
)
PetriNetModel_Node_strategy = st.builds(
    PetriNetModel_Node,
    name=
        safe_text
)
PetriNetModel_PObject_strategy = st.builds(
    PetriNetModel_PObject,
    id=
        st.integers()
)
PetriNetModel_PetriNet_strategy = st.builds(
    PetriNetModel_PetriNet,
)
PetriNetModel_Token_strategy = st.builds(
    PetriNetModel_Token,
)
Node_strategy = st.builds(
    Node,
)
PetriNetModel_Place_strategy = st.builds(
    PetriNetModel_Place,
)
PetriNetModel_Transition_strategy = st.builds(
    PetriNetModel_Transition,
)

@given(instance=PObject_strategy)
@settings(max_examples=50)
def test_pobject_instantiation(instance):
    assert isinstance(instance, PObject)

@given(instance=PetriNetModel_Arc_strategy)
@settings(max_examples=50)
def test_petrinetmodel_arc_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Arc)

@given(instance=PetriNetModel_Node_strategy)
@settings(max_examples=50)
def test_petrinetmodel_node_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Node)



@given(instance=PetriNetModel_Node_strategy)
def test_petrinetmodel_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetModel_PObject_strategy)
@settings(max_examples=50)
def test_petrinetmodel_pobject_instantiation(instance):
    assert isinstance(instance, PetriNetModel_PObject)



@given(instance=PetriNetModel_PObject_strategy)
def test_petrinetmodel_pobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PetriNetModel_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetmodel_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNetModel_PetriNet)

@given(instance=PetriNetModel_Token_strategy)
@settings(max_examples=50)
def test_petrinetmodel_token_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNetModel_Place_strategy)
@settings(max_examples=50)
def test_petrinetmodel_place_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Place)

@given(instance=PetriNetModel_Transition_strategy)
@settings(max_examples=50)
def test_petrinetmodel_transition_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Transition)
