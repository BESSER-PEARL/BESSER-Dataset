import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet_PetriModel,
    PetriEdge,
    PetriNet_Arc,
    PetriNode,
    PetriNet_Token,
    PetriNet_Transition,
    PetriNet_Place,
    PetriModel,
    PetriNet_PetriEdge,
    PetriNet_PetriNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_petrimodel_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriModel)


def test_petrinet_petrimodel_constructor_exists():
    assert callable(PetriNet_PetriModel.__init__)


def test_petrinet_petrimodel_constructor_args():
    sig = inspect.signature(PetriNet_PetriModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_petrinet_petrimodel_has_name():
    assert hasattr(PetriNet_PetriModel, "name")
    descriptor = None
    for klass in PetriNet_PetriModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_petrimodel_has_description():
    assert hasattr(PetriNet_PetriModel, "description")
    descriptor = None
    for klass in PetriNet_PetriModel.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_petriedge_is_not_abstract():
    assert not inspect.isabstract(PetriEdge)


def test_petriedge_constructor_exists():
    assert callable(PetriEdge.__init__)


def test_petriedge_constructor_args():
    sig = inspect.signature(PetriEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinode_is_not_abstract():
    assert not inspect.isabstract(PetriNode)


def test_petrinode_constructor_exists():
    assert callable(PetriNode.__init__)


def test_petrinode_constructor_args():
    sig = inspect.signature(PetriNode.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_token_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Token)


def test_petrinet_token_constructor_exists():
    assert callable(PetriNet_Token.__init__)


def test_petrinet_token_constructor_args():
    sig = inspect.signature(PetriNet_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrimodel_is_not_abstract():
    assert not inspect.isabstract(PetriModel)


def test_petrimodel_constructor_exists():
    assert callable(PetriModel.__init__)


def test_petrimodel_constructor_args():
    sig = inspect.signature(PetriModel.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petriedge_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriEdge)


def test_petrinet_petriedge_constructor_exists():
    assert callable(PetriNet_PetriEdge.__init__)


def test_petrinet_petriedge_constructor_args():
    sig = inspect.signature(PetriNet_PetriEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinode_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNode)


def test_petrinet_petrinode_constructor_exists():
    assert callable(PetriNet_PetriNode.__init__)


def test_petrinet_petrinode_constructor_args():
    sig = inspect.signature(PetriNet_PetriNode.__init__)
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
PetriNet_PetriModel_strategy = st.builds(
    PetriNet_PetriModel,
    name=
        safe_text,
    description=
        safe_text
)
PetriEdge_strategy = st.builds(
    PetriEdge,
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
)
PetriNode_strategy = st.builds(
    PetriNode,
)
PetriNet_Token_strategy = st.builds(
    PetriNet_Token,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriModel_strategy = st.builds(
    PetriModel,
)
PetriNet_PetriEdge_strategy = st.builds(
    PetriNet_PetriEdge,
)
PetriNet_PetriNode_strategy = st.builds(
    PetriNet_PetriNode,
)

@given(instance=PetriNet_PetriModel_strategy)
@settings(max_examples=50)
def test_petrinet_petrimodel_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriModel)



@given(instance=PetriNet_PetriModel_strategy)
def test_petrinet_petrimodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetriNet_PetriModel_strategy)
def test_petrinet_petrimodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PetriEdge_strategy)
@settings(max_examples=50)
def test_petriedge_instantiation(instance):
    assert isinstance(instance, PetriEdge)

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)

@given(instance=PetriNode_strategy)
@settings(max_examples=50)
def test_petrinode_instantiation(instance):
    assert isinstance(instance, PetriNode)

@given(instance=PetriNet_Token_strategy)
@settings(max_examples=50)
def test_petrinet_token_instantiation(instance):
    assert isinstance(instance, PetriNet_Token)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)

@given(instance=PetriModel_strategy)
@settings(max_examples=50)
def test_petrimodel_instantiation(instance):
    assert isinstance(instance, PetriModel)

@given(instance=PetriNet_PetriEdge_strategy)
@settings(max_examples=50)
def test_petrinet_petriedge_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriEdge)

@given(instance=PetriNet_PetriNode_strategy)
@settings(max_examples=50)
def test_petrinet_petrinode_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNode)
