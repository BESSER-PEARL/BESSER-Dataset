import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriModel,
    PetriNet::PetriNode,
    PetriNet::PetriEdge,
    PetriNet::PetriModel,
    PetriEdge,
    PetriNet::Arc,
    PetriNode,
    PetriNet::Place,
    PetriNet::Transition,
    PetriNet::Token,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrimodel_is_not_abstract():
    assert not inspect.isabstract(PetriModel)


def test_petrimodel_constructor_exists():
    assert callable(PetriModel.__init__)


def test_petrimodel_constructor_args():
    sig = inspect.signature(PetriModel.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinode_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNode)


def test_petrinet::petrinode_constructor_exists():
    assert callable(PetriNet::PetriNode.__init__)


def test_petrinet::petrinode_constructor_args():
    sig = inspect.signature(PetriNet::PetriNode.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petriedge_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriEdge)


def test_petrinet::petriedge_constructor_exists():
    assert callable(PetriNet::PetriEdge.__init__)


def test_petrinet::petriedge_constructor_args():
    sig = inspect.signature(PetriNet::PetriEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrimodel_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriModel)


def test_petrinet::petrimodel_constructor_exists():
    assert callable(PetriNet::PetriModel.__init__)


def test_petrinet::petrimodel_constructor_args():
    sig = inspect.signature(PetriNet::PetriModel.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrimodel_has_description():
    assert hasattr(PetriNet::PetriModel, "description")
    descriptor = None
    for klass in PetriNet::PetriModel.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::petrimodel_has_name():
    assert hasattr(PetriNet::PetriModel, "name")
    descriptor = None
    for klass in PetriNet::PetriModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petriedge_is_not_abstract():
    assert not inspect.isabstract(PetriEdge)


def test_petriedge_constructor_exists():
    assert callable(PetriEdge.__init__)


def test_petriedge_constructor_args():
    sig = inspect.signature(PetriEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(PetriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(PetriNet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinode_is_not_abstract():
    assert not inspect.isabstract(PetriNode)


def test_petrinode_constructor_exists():
    assert callable(PetriNode.__init__)


def test_petrinode_constructor_args():
    sig = inspect.signature(PetriNode.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::token_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Token)


def test_petrinet::token_constructor_exists():
    assert callable(PetriNet::Token.__init__)


def test_petrinet::token_constructor_args():
    sig = inspect.signature(PetriNet::Token.__init__)
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
PetriModel_strategy = st.builds(
    PetriModel,
)
PetriNet::PetriNode_strategy = st.builds(
    PetriNet::PetriNode,
)
PetriNet::PetriEdge_strategy = st.builds(
    PetriNet::PetriEdge,
)
PetriNet::PetriModel_strategy = st.builds(
    PetriNet::PetriModel,
    description=
        safe_text,
    name=
        safe_text
)
PetriEdge_strategy = st.builds(
    PetriEdge,
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
)
PetriNode_strategy = st.builds(
    PetriNode,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::Token_strategy = st.builds(
    PetriNet::Token,
)

@given(instance=PetriModel_strategy)
@settings(max_examples=50)
def test_petrimodel_instantiation(instance):
    assert isinstance(instance, PetriModel)

@given(instance=PetriNet::PetriNode_strategy)
@settings(max_examples=50)
def test_petrinet::petrinode_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNode)

@given(instance=PetriNet::PetriEdge_strategy)
@settings(max_examples=50)
def test_petrinet::petriedge_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriEdge)

@given(instance=PetriNet::PetriModel_strategy)
@settings(max_examples=50)
def test_petrinet::petrimodel_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriModel)

@given(instance=PetriNet::PetriModel_strategy)
def test_petrinet::petrimodel_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=PetriNet::PetriModel_strategy)
def test_petrinet::petrimodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PetriNet::PetriModel_strategy)
def test_petrinet::petrimodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::PetriModel_strategy)
def test_petrinet::petrimodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriEdge_strategy)
@settings(max_examples=50)
def test_petriedge_instantiation(instance):
    assert isinstance(instance, PetriEdge)

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNode_strategy)
@settings(max_examples=50)
def test_petrinode_instantiation(instance):
    assert isinstance(instance, PetriNode)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Token_strategy)
@settings(max_examples=50)
def test_petrinet::token_instantiation(instance):
    assert isinstance(instance, PetriNet::Token)
