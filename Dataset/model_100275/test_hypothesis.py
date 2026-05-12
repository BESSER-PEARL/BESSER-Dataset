import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet_Token,
    Arc,
    PetriNet_TPArc,
    PetriNet_PTArc,
    PetriNet_Arc,
    Transition,
    Place,
    PetriNet_Net,
    PetriNet_Transition,
    Token,
    TPArc,
    PTArc,
    Net,
    PetriNet_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_token_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Token)


def test_petrinet_token_constructor_exists():
    assert callable(PetriNet_Token.__init__)


def test_petrinet_token_constructor_args():
    sig = inspect.signature(PetriNet_Token.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_TPArc)


def test_petrinet_tparc_constructor_exists():
    assert callable(PetriNet_TPArc.__init__)


def test_petrinet_tparc_constructor_args():
    sig = inspect.signature(PetriNet_TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PTArc)


def test_petrinet_ptarc_constructor_exists():
    assert callable(PetriNet_PTArc.__init__)


def test_petrinet_ptarc_constructor_args():
    sig = inspect.signature(PetriNet_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_arc_has_weight():
    assert hasattr(PetriNet_Arc, "weight")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Net)


def test_petrinet_net_constructor_exists():
    assert callable(PetriNet_Net.__init__)


def test_petrinet_net_constructor_args():
    sig = inspect.signature(PetriNet_Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_token_is_not_abstract():
    assert not inspect.isabstract(Token)


def test_token_constructor_exists():
    assert callable(Token.__init__)


def test_token_constructor_args():
    sig = inspect.signature(Token.__init__)
    params = list(sig.parameters.keys())



def test_tparc_is_not_abstract():
    assert not inspect.isabstract(TPArc)


def test_tparc_constructor_exists():
    assert callable(TPArc.__init__)


def test_tparc_constructor_args():
    sig = inspect.signature(TPArc.__init__)
    params = list(sig.parameters.keys())



def test_ptarc_is_not_abstract():
    assert not inspect.isabstract(PTArc)


def test_ptarc_constructor_exists():
    assert callable(PTArc.__init__)


def test_ptarc_constructor_args():
    sig = inspect.signature(PTArc.__init__)
    params = list(sig.parameters.keys())



def test_net_is_not_abstract():
    assert not inspect.isabstract(Net)


def test_net_constructor_exists():
    assert callable(Net.__init__)


def test_net_constructor_args():
    sig = inspect.signature(Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
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
PetriNet_Token_strategy = st.builds(
    PetriNet_Token,
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet_TPArc_strategy = st.builds(
    PetriNet_TPArc,
)
PetriNet_PTArc_strategy = st.builds(
    PetriNet_PTArc,
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    weight=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
PetriNet_Net_strategy = st.builds(
    PetriNet_Net,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
Token_strategy = st.builds(
    Token,
)
TPArc_strategy = st.builds(
    TPArc,
)
PTArc_strategy = st.builds(
    PTArc,
)
Net_strategy = st.builds(
    Net,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)

@given(instance=PetriNet_Token_strategy)
@settings(max_examples=50)
def test_petrinet_token_instantiation(instance):
    assert isinstance(instance, PetriNet_Token)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet_TPArc_strategy)
@settings(max_examples=50)
def test_petrinet_tparc_instantiation(instance):
    assert isinstance(instance, PetriNet_TPArc)

@given(instance=PetriNet_PTArc_strategy)
@settings(max_examples=50)
def test_petrinet_ptarc_instantiation(instance):
    assert isinstance(instance, PetriNet_PTArc)

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PetriNet_Net_strategy)
@settings(max_examples=50)
def test_petrinet_net_instantiation(instance):
    assert isinstance(instance, PetriNet_Net)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=Token_strategy)
@settings(max_examples=50)
def test_token_instantiation(instance):
    assert isinstance(instance, Token)

@given(instance=TPArc_strategy)
@settings(max_examples=50)
def test_tparc_instantiation(instance):
    assert isinstance(instance, TPArc)

@given(instance=PTArc_strategy)
@settings(max_examples=50)
def test_ptarc_instantiation(instance):
    assert isinstance(instance, PTArc)

@given(instance=Net_strategy)
@settings(max_examples=50)
def test_net_instantiation(instance):
    assert isinstance(instance, Net)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)
