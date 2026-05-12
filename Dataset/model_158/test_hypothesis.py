import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    petrinet_TPArc,
    petrinet_PTArc,
    petrinet_Token,
    petrinet_Arc,
    petrinet_Transition,
    petrinet_Place,
    petrinet_Petrinet,
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



def test_petrinet_tparc_is_not_abstract():
    assert not inspect.isabstract(petrinet_TPArc)


def test_petrinet_tparc_constructor_exists():
    assert callable(petrinet_TPArc.__init__)


def test_petrinet_tparc_constructor_args():
    sig = inspect.signature(petrinet_TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_ptarc_is_not_abstract():
    assert not inspect.isabstract(petrinet_PTArc)


def test_petrinet_ptarc_constructor_exists():
    assert callable(petrinet_PTArc.__init__)


def test_petrinet_ptarc_constructor_args():
    sig = inspect.signature(petrinet_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_token_is_not_abstract():
    assert not inspect.isabstract(petrinet_Token)


def test_petrinet_token_constructor_exists():
    assert callable(petrinet_Token.__init__)


def test_petrinet_token_constructor_args():
    sig = inspect.signature(petrinet_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_arc_has_weight():
    assert hasattr(petrinet_Arc, "weight")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_name():
    assert hasattr(petrinet_Arc, "name")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_transition_has_name():
    assert hasattr(petrinet_Transition, "name")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_place_has_name():
    assert hasattr(petrinet_Place, "name")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_Petrinet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_Petrinet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_Petrinet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(petrinet_Petrinet, "name")
    descriptor = None
    for klass in petrinet_Petrinet.__mro__:
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
Arc_strategy = st.builds(
    Arc,
)
petrinet_TPArc_strategy = st.builds(
    petrinet_TPArc,
)
petrinet_PTArc_strategy = st.builds(
    petrinet_PTArc,
)
petrinet_Token_strategy = st.builds(
    petrinet_Token,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    weight=
        st.integers(),
    name=
        safe_text
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
    name=
        safe_text
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    name=
        safe_text
)
petrinet_Petrinet_strategy = st.builds(
    petrinet_Petrinet,
    name=
        safe_text
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet_TPArc_strategy)
@settings(max_examples=50)
def test_petrinet_tparc_instantiation(instance):
    assert isinstance(instance, petrinet_TPArc)

@given(instance=petrinet_PTArc_strategy)
@settings(max_examples=50)
def test_petrinet_ptarc_instantiation(instance):
    assert isinstance(instance, petrinet_PTArc)

@given(instance=petrinet_Token_strategy)
@settings(max_examples=50)
def test_petrinet_token_instantiation(instance):
    assert isinstance(instance, petrinet_Token)

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_Petrinet)



@given(instance=petrinet_Petrinet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
