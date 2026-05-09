import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PObject,
    PetriNetModel::Arc,
    PetriNetModel::Node,
    PetriNetModel::PObject,
    PetriNetModel::PetriNet,
    PetriNetModel::Token,
    Node,
    PetriNetModel::Place,
    PetriNetModel::Transition,
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



def test_petrinetmodel::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Arc)


def test_petrinetmodel::arc_constructor_exists():
    assert callable(PetriNetModel::Arc.__init__)


def test_petrinetmodel::arc_constructor_args():
    sig = inspect.signature(PetriNetModel::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel::node_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Node)


def test_petrinetmodel::node_constructor_exists():
    assert callable(PetriNetModel::Node.__init__)


def test_petrinetmodel::node_constructor_args():
    sig = inspect.signature(PetriNetModel::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmodel::node_has_name():
    assert hasattr(PetriNetModel::Node, "name")
    descriptor = None
    for klass in PetriNetModel::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel::pobject_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::PObject)


def test_petrinetmodel::pobject_constructor_exists():
    assert callable(PetriNetModel::PObject.__init__)


def test_petrinetmodel::pobject_constructor_args():
    sig = inspect.signature(PetriNetModel::PObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_petrinetmodel::pobject_has_id():
    assert hasattr(PetriNetModel::PObject, "id")
    descriptor = None
    for klass in PetriNetModel::PObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::PetriNet)


def test_petrinetmodel::petrinet_constructor_exists():
    assert callable(PetriNetModel::PetriNet.__init__)


def test_petrinetmodel::petrinet_constructor_args():
    sig = inspect.signature(PetriNetModel::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel::token_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Token)


def test_petrinetmodel::token_constructor_exists():
    assert callable(PetriNetModel::Token.__init__)


def test_petrinetmodel::token_constructor_args():
    sig = inspect.signature(PetriNetModel::Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel::place_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Place)


def test_petrinetmodel::place_constructor_exists():
    assert callable(PetriNetModel::Place.__init__)


def test_petrinetmodel::place_constructor_args():
    sig = inspect.signature(PetriNetModel::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodel::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Transition)


def test_petrinetmodel::transition_constructor_exists():
    assert callable(PetriNetModel::Transition.__init__)


def test_petrinetmodel::transition_constructor_args():
    sig = inspect.signature(PetriNetModel::Transition.__init__)
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
PetriNetModel::Arc_strategy = st.builds(
    PetriNetModel::Arc,
)
PetriNetModel::Node_strategy = st.builds(
    PetriNetModel::Node,
    name=
        safe_text
)
PetriNetModel::PObject_strategy = st.builds(
    PetriNetModel::PObject,
    id=
        st.integers()
)
PetriNetModel::PetriNet_strategy = st.builds(
    PetriNetModel::PetriNet,
)
PetriNetModel::Token_strategy = st.builds(
    PetriNetModel::Token,
)
Node_strategy = st.builds(
    Node,
)
PetriNetModel::Place_strategy = st.builds(
    PetriNetModel::Place,
)
PetriNetModel::Transition_strategy = st.builds(
    PetriNetModel::Transition,
)

@given(instance=PObject_strategy)
@settings(max_examples=50)
def test_pobject_instantiation(instance):
    assert isinstance(instance, PObject)

@given(instance=PetriNetModel::Arc_strategy)
@settings(max_examples=50)
def test_petrinetmodel::arc_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Arc)

@given(instance=PetriNetModel::Node_strategy)
@settings(max_examples=50)
def test_petrinetmodel::node_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Node)

@given(instance=PetriNetModel::Node_strategy)
def test_petrinetmodel::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetModel::Node_strategy)
def test_petrinetmodel::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetModel::PObject_strategy)
@settings(max_examples=50)
def test_petrinetmodel::pobject_instantiation(instance):
    assert isinstance(instance, PetriNetModel::PObject)

@given(instance=PetriNetModel::PObject_strategy)
def test_petrinetmodel::pobject_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=PetriNetModel::PObject_strategy)
def test_petrinetmodel::pobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PetriNetModel::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetmodel::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNetModel::PetriNet)

@given(instance=PetriNetModel::Token_strategy)
@settings(max_examples=50)
def test_petrinetmodel::token_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNetModel::Place_strategy)
@settings(max_examples=50)
def test_petrinetmodel::place_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Place)

@given(instance=PetriNetModel::Transition_strategy)
@settings(max_examples=50)
def test_petrinetmodel::transition_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Transition)
