import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNetModel::PetriNet,
    PetriNetModel::Place,
    PetriNetModel::ArcTP,
    PetriNetModel::ArcPT,
    PetriNetModel::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetmodel::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::PetriNet)


def test_petrinetmodel::petrinet_constructor_exists():
    assert callable(PetriNetModel::PetriNet.__init__)


def test_petrinetmodel::petrinet_constructor_args():
    sig = inspect.signature(PetriNetModel::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmodel::petrinet_has_name():
    assert hasattr(PetriNetModel::PetriNet, "name")
    descriptor = None
    for klass in PetriNetModel::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel::place_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Place)


def test_petrinetmodel::place_constructor_exists():
    assert callable(PetriNetModel::Place.__init__)


def test_petrinetmodel::place_constructor_args():
    sig = inspect.signature(PetriNetModel::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "token" in params, "Missing parameter 'token'"

def test_petrinetmodel::place_has_name():
    assert hasattr(PetriNetModel::Place, "name")
    descriptor = None
    for klass in PetriNetModel::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetmodel::place_has_token():
    assert hasattr(PetriNetModel::Place, "token")
    descriptor = None
    for klass in PetriNetModel::Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel::arctp_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::ArcTP)


def test_petrinetmodel::arctp_constructor_exists():
    assert callable(PetriNetModel::ArcTP.__init__)


def test_petrinetmodel::arctp_constructor_args():
    sig = inspect.signature(PetriNetModel::ArcTP.__init__)
    params = list(sig.parameters.keys())
    assert "inscription" in params, "Missing parameter 'inscription'"

def test_petrinetmodel::arctp_has_inscription():
    assert hasattr(PetriNetModel::ArcTP, "inscription")
    descriptor = None
    for klass in PetriNetModel::ArcTP.__mro__:
        if "inscription" in klass.__dict__:
            descriptor = klass.__dict__["inscription"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel::arcpt_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::ArcPT)


def test_petrinetmodel::arcpt_constructor_exists():
    assert callable(PetriNetModel::ArcPT.__init__)


def test_petrinetmodel::arcpt_constructor_args():
    sig = inspect.signature(PetriNetModel::ArcPT.__init__)
    params = list(sig.parameters.keys())
    assert "inscription" in params, "Missing parameter 'inscription'"

def test_petrinetmodel::arcpt_has_inscription():
    assert hasattr(PetriNetModel::ArcPT, "inscription")
    descriptor = None
    for klass in PetriNetModel::ArcPT.__mro__:
        if "inscription" in klass.__dict__:
            descriptor = klass.__dict__["inscription"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel::Transition)


def test_petrinetmodel::transition_constructor_exists():
    assert callable(PetriNetModel::Transition.__init__)


def test_petrinetmodel::transition_constructor_args():
    sig = inspect.signature(PetriNetModel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmodel::transition_has_name():
    assert hasattr(PetriNetModel::Transition, "name")
    descriptor = None
    for klass in PetriNetModel::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
PetriNetModel::PetriNet_strategy = st.builds(
    PetriNetModel::PetriNet,
    name=
        safe_text
)
PetriNetModel::Place_strategy = st.builds(
    PetriNetModel::Place,
    name=
        safe_text,
    token=
        safe_text
)
PetriNetModel::ArcTP_strategy = st.builds(
    PetriNetModel::ArcTP,
    inscription=
        safe_text
)
PetriNetModel::ArcPT_strategy = st.builds(
    PetriNetModel::ArcPT,
    inscription=
        safe_text
)
PetriNetModel::Transition_strategy = st.builds(
    PetriNetModel::Transition,
    name=
        safe_text
)

@given(instance=PetriNetModel::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetmodel::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNetModel::PetriNet)

@given(instance=PetriNetModel::PetriNet_strategy)
def test_petrinetmodel::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetModel::PetriNet_strategy)
def test_petrinetmodel::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetModel::Place_strategy)
@settings(max_examples=50)
def test_petrinetmodel::place_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Place)

@given(instance=PetriNetModel::Place_strategy)
def test_petrinetmodel::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetModel::Place_strategy)
def test_petrinetmodel::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetModel::Place_strategy)
def test_petrinetmodel::place_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=PetriNetModel::Place_strategy)
def test_petrinetmodel::place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=PetriNetModel::ArcTP_strategy)
@settings(max_examples=50)
def test_petrinetmodel::arctp_instantiation(instance):
    assert isinstance(instance, PetriNetModel::ArcTP)

@given(instance=PetriNetModel::ArcTP_strategy)
def test_petrinetmodel::arctp_inscription_type(instance):
    assert isinstance(instance.inscription, str)


@given(instance=PetriNetModel::ArcTP_strategy)
def test_petrinetmodel::arctp_inscription_setter(instance):
    original = instance.inscription
    instance.inscription = original
    assert instance.inscription == original

@given(instance=PetriNetModel::ArcPT_strategy)
@settings(max_examples=50)
def test_petrinetmodel::arcpt_instantiation(instance):
    assert isinstance(instance, PetriNetModel::ArcPT)

@given(instance=PetriNetModel::ArcPT_strategy)
def test_petrinetmodel::arcpt_inscription_type(instance):
    assert isinstance(instance.inscription, str)


@given(instance=PetriNetModel::ArcPT_strategy)
def test_petrinetmodel::arcpt_inscription_setter(instance):
    original = instance.inscription
    instance.inscription = original
    assert instance.inscription == original

@given(instance=PetriNetModel::Transition_strategy)
@settings(max_examples=50)
def test_petrinetmodel::transition_instantiation(instance):
    assert isinstance(instance, PetriNetModel::Transition)

@given(instance=PetriNetModel::Transition_strategy)
def test_petrinetmodel::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetModel::Transition_strategy)
def test_petrinetmodel::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
