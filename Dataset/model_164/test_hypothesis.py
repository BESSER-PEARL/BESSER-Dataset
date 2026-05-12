import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Identifiable,
    PetriNet_Net,
    PetriNet_Place,
    PetriNet_Transition,
    PetriNet_OutputArc,
    PetriNet_InputArc,
    PetriNet_Token,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Net)


def test_petrinet_net_constructor_exists():
    assert callable(PetriNet_Net.__init__)


def test_petrinet_net_constructor_args():
    sig = inspect.signature(PetriNet_Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_place_has_name():
    assert hasattr(PetriNet_Place, "name")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_transition_has_name():
    assert hasattr(PetriNet_Transition, "name")
    descriptor = None
    for klass in PetriNet_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_outputarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_OutputArc)


def test_petrinet_outputarc_constructor_exists():
    assert callable(PetriNet_OutputArc.__init__)


def test_petrinet_outputarc_constructor_args():
    sig = inspect.signature(PetriNet_OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_inputarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_InputArc)


def test_petrinet_inputarc_constructor_exists():
    assert callable(PetriNet_InputArc.__init__)


def test_petrinet_inputarc_constructor_args():
    sig = inspect.signature(PetriNet_InputArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_token_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Token)


def test_petrinet_token_constructor_exists():
    assert callable(PetriNet_Token.__init__)


def test_petrinet_token_constructor_args():
    sig = inspect.signature(PetriNet_Token.__init__)
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
Identifiable_strategy = st.builds(
    Identifiable,
)
PetriNet_Net_strategy = st.builds(
    PetriNet_Net,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    name=
        safe_text
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
    name=
        safe_text
)
PetriNet_OutputArc_strategy = st.builds(
    PetriNet_OutputArc,
)
PetriNet_InputArc_strategy = st.builds(
    PetriNet_InputArc,
)
PetriNet_Token_strategy = st.builds(
    PetriNet_Token,
)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=PetriNet_Net_strategy)
@settings(max_examples=50)
def test_petrinet_net_instantiation(instance):
    assert isinstance(instance, PetriNet_Net)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)



@given(instance=PetriNet_Transition_strategy)
def test_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet_outputarc_instantiation(instance):
    assert isinstance(instance, PetriNet_OutputArc)

@given(instance=PetriNet_InputArc_strategy)
@settings(max_examples=50)
def test_petrinet_inputarc_instantiation(instance):
    assert isinstance(instance, PetriNet_InputArc)

@given(instance=PetriNet_Token_strategy)
@settings(max_examples=50)
def test_petrinet_token_instantiation(instance):
    assert isinstance(instance, PetriNet_Token)
