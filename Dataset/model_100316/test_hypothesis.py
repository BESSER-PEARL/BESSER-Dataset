import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNetModel_ArcPT,
    PetriNetModel_Transition,
    PetriNetModel_PetriNet,
    PetriNetModel_Place,
    PetriNetModel_ArcTP,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetmodel_arcpt_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_ArcPT)


def test_petrinetmodel_arcpt_constructor_exists():
    assert callable(PetriNetModel_ArcPT.__init__)


def test_petrinetmodel_arcpt_constructor_args():
    sig = inspect.signature(PetriNetModel_ArcPT.__init__)
    params = list(sig.parameters.keys())
    assert "inscription" in params, "Missing parameter 'inscription'"

def test_petrinetmodel_arcpt_has_inscription():
    assert hasattr(PetriNetModel_ArcPT, "inscription")
    descriptor = None
    for klass in PetriNetModel_ArcPT.__mro__:
        if "inscription" in klass.__dict__:
            descriptor = klass.__dict__["inscription"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Transition)


def test_petrinetmodel_transition_constructor_exists():
    assert callable(PetriNetModel_Transition.__init__)


def test_petrinetmodel_transition_constructor_args():
    sig = inspect.signature(PetriNetModel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmodel_transition_has_name():
    assert hasattr(PetriNetModel_Transition, "name")
    descriptor = None
    for klass in PetriNetModel_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_PetriNet)


def test_petrinetmodel_petrinet_constructor_exists():
    assert callable(PetriNetModel_PetriNet.__init__)


def test_petrinetmodel_petrinet_constructor_args():
    sig = inspect.signature(PetriNetModel_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmodel_petrinet_has_name():
    assert hasattr(PetriNetModel_PetriNet, "name")
    descriptor = None
    for klass in PetriNetModel_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_place_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_Place)


def test_petrinetmodel_place_constructor_exists():
    assert callable(PetriNetModel_Place.__init__)


def test_petrinetmodel_place_constructor_args():
    sig = inspect.signature(PetriNetModel_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "token" in params, "Missing parameter 'token'"

def test_petrinetmodel_place_has_name():
    assert hasattr(PetriNetModel_Place, "name")
    descriptor = None
    for klass in PetriNetModel_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetmodel_place_has_token():
    assert hasattr(PetriNetModel_Place, "token")
    descriptor = None
    for klass in PetriNetModel_Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_arctp_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel_ArcTP)


def test_petrinetmodel_arctp_constructor_exists():
    assert callable(PetriNetModel_ArcTP.__init__)


def test_petrinetmodel_arctp_constructor_args():
    sig = inspect.signature(PetriNetModel_ArcTP.__init__)
    params = list(sig.parameters.keys())
    assert "inscription" in params, "Missing parameter 'inscription'"

def test_petrinetmodel_arctp_has_inscription():
    assert hasattr(PetriNetModel_ArcTP, "inscription")
    descriptor = None
    for klass in PetriNetModel_ArcTP.__mro__:
        if "inscription" in klass.__dict__:
            descriptor = klass.__dict__["inscription"]
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
PetriNetModel_ArcPT_strategy = st.builds(
    PetriNetModel_ArcPT,
    inscription=
        safe_text
)
PetriNetModel_Transition_strategy = st.builds(
    PetriNetModel_Transition,
    name=
        safe_text
)
PetriNetModel_PetriNet_strategy = st.builds(
    PetriNetModel_PetriNet,
    name=
        safe_text
)
PetriNetModel_Place_strategy = st.builds(
    PetriNetModel_Place,
    name=
        safe_text,
    token=
        safe_text
)
PetriNetModel_ArcTP_strategy = st.builds(
    PetriNetModel_ArcTP,
    inscription=
        safe_text
)

@given(instance=PetriNetModel_ArcPT_strategy)
@settings(max_examples=50)
def test_petrinetmodel_arcpt_instantiation(instance):
    assert isinstance(instance, PetriNetModel_ArcPT)



@given(instance=PetriNetModel_ArcPT_strategy)
def test_petrinetmodel_arcpt_inscription_setter(instance):
    original = instance.inscription
    instance.inscription = original
    assert instance.inscription == original

@given(instance=PetriNetModel_Transition_strategy)
@settings(max_examples=50)
def test_petrinetmodel_transition_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Transition)



@given(instance=PetriNetModel_Transition_strategy)
def test_petrinetmodel_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetModel_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetmodel_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNetModel_PetriNet)



@given(instance=PetriNetModel_PetriNet_strategy)
def test_petrinetmodel_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetModel_Place_strategy)
@settings(max_examples=50)
def test_petrinetmodel_place_instantiation(instance):
    assert isinstance(instance, PetriNetModel_Place)



@given(instance=PetriNetModel_Place_strategy)
def test_petrinetmodel_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetriNetModel_Place_strategy)
def test_petrinetmodel_place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=PetriNetModel_ArcTP_strategy)
@settings(max_examples=50)
def test_petrinetmodel_arctp_instantiation(instance):
    assert isinstance(instance, PetriNetModel_ArcTP)



@given(instance=PetriNetModel_ArcTP_strategy)
def test_petrinetmodel_arctp_inscription_setter(instance):
    original = instance.inscription
    instance.inscription = original
    assert instance.inscription == original
