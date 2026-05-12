import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    lit::petriNets::Arc,
    lit::petriNets::Transition,
    lit::petriNets::Place,
    lit::petriNets::Net,
    lit::petriNets::PTArc,
    lit::petriNets::TPArc,
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



def test_lit::petrinets::arc_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Arc)


def test_lit::petrinets::arc_constructor_exists():
    assert callable(lit::petriNets::Arc.__init__)


def test_lit::petrinets::arc_constructor_args():
    sig = inspect.signature(lit::petriNets::Arc.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Transition)


def test_lit::petrinets::transition_constructor_exists():
    assert callable(lit::petriNets::Transition.__init__)


def test_lit::petrinets::transition_constructor_args():
    sig = inspect.signature(lit::petriNets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit::petrinets::transition_has_name():
    assert hasattr(lit::petriNets::Transition, "name")
    descriptor = None
    for klass in lit::petriNets::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit::petrinets::place_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Place)


def test_lit::petrinets::place_constructor_exists():
    assert callable(lit::petriNets::Place.__init__)


def test_lit::petrinets::place_constructor_args():
    sig = inspect.signature(lit::petriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit::petrinets::place_has_name():
    assert hasattr(lit::petriNets::Place, "name")
    descriptor = None
    for klass in lit::petriNets::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit::petrinets::net_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Net)


def test_lit::petrinets::net_constructor_exists():
    assert callable(lit::petriNets::Net.__init__)


def test_lit::petrinets::net_constructor_args():
    sig = inspect.signature(lit::petriNets::Net.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::ptarc_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::PTArc)


def test_lit::petrinets::ptarc_constructor_exists():
    assert callable(lit::petriNets::PTArc.__init__)


def test_lit::petrinets::ptarc_constructor_args():
    sig = inspect.signature(lit::petriNets::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::tparc_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::TPArc)


def test_lit::petrinets::tparc_constructor_exists():
    assert callable(lit::petriNets::TPArc.__init__)


def test_lit::petrinets::tparc_constructor_args():
    sig = inspect.signature(lit::petriNets::TPArc.__init__)
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
Arc_strategy = st.builds(
    Arc,
)
lit::petriNets::Arc_strategy = st.builds(
    lit::petriNets::Arc,
)
lit::petriNets::Transition_strategy = st.builds(
    lit::petriNets::Transition,
    name=
        safe_text
)
lit::petriNets::Place_strategy = st.builds(
    lit::petriNets::Place,
    name=
        safe_text
)
lit::petriNets::Net_strategy = st.builds(
    lit::petriNets::Net,
)
lit::petriNets::PTArc_strategy = st.builds(
    lit::petriNets::PTArc,
)
lit::petriNets::TPArc_strategy = st.builds(
    lit::petriNets::TPArc,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=lit::petriNets::Arc_strategy)
@settings(max_examples=50)
def test_lit::petrinets::arc_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Arc)

@given(instance=lit::petriNets::Transition_strategy)
@settings(max_examples=50)
def test_lit::petrinets::transition_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Transition)

@given(instance=lit::petriNets::Transition_strategy)
def test_lit::petrinets::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lit::petriNets::Transition_strategy)
def test_lit::petrinets::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit::petriNets::Place_strategy)
@settings(max_examples=50)
def test_lit::petrinets::place_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Place)

@given(instance=lit::petriNets::Place_strategy)
def test_lit::petrinets::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lit::petriNets::Place_strategy)
def test_lit::petrinets::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit::petriNets::Net_strategy)
@settings(max_examples=50)
def test_lit::petrinets::net_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Net)

@given(instance=lit::petriNets::PTArc_strategy)
@settings(max_examples=50)
def test_lit::petrinets::ptarc_instantiation(instance):
    assert isinstance(instance, lit::petriNets::PTArc)

@given(instance=lit::petriNets::TPArc_strategy)
@settings(max_examples=50)
def test_lit::petrinets::tparc_instantiation(instance):
    assert isinstance(instance, lit::petriNets::TPArc)
