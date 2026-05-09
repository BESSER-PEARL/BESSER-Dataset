import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lit::petriNets::2::Arc,
    lit::petriNets::2::Transition,
    Arc,
    lit::petriNets::2::TPArc,
    lit::petriNets::2::PTArc,
    lit::petriNets::2::Place,
    lit::petriNets::2::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lit::petrinets::2::arc_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::2::Arc)


def test_lit::petrinets::2::arc_constructor_exists():
    assert callable(lit::petriNets::2::Arc.__init__)


def test_lit::petrinets::2::arc_constructor_args():
    sig = inspect.signature(lit::petriNets::2::Arc.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::2::transition_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::2::Transition)


def test_lit::petrinets::2::transition_constructor_exists():
    assert callable(lit::petriNets::2::Transition.__init__)


def test_lit::petrinets::2::transition_constructor_args():
    sig = inspect.signature(lit::petriNets::2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit::petrinets::2::transition_has_name():
    assert hasattr(lit::petriNets::2::Transition, "name")
    descriptor = None
    for klass in lit::petriNets::2::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::2::tparc_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::2::TPArc)


def test_lit::petrinets::2::tparc_constructor_exists():
    assert callable(lit::petriNets::2::TPArc.__init__)


def test_lit::petrinets::2::tparc_constructor_args():
    sig = inspect.signature(lit::petriNets::2::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::2::ptarc_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::2::PTArc)


def test_lit::petrinets::2::ptarc_constructor_exists():
    assert callable(lit::petriNets::2::PTArc.__init__)


def test_lit::petrinets::2::ptarc_constructor_args():
    sig = inspect.signature(lit::petriNets::2::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_lit::petrinets::2::place_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::2::Place)


def test_lit::petrinets::2::place_constructor_exists():
    assert callable(lit::petriNets::2::Place.__init__)


def test_lit::petrinets::2::place_constructor_args():
    sig = inspect.signature(lit::petriNets::2::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit::petrinets::2::place_has_name():
    assert hasattr(lit::petriNets::2::Place, "name")
    descriptor = None
    for klass in lit::petriNets::2::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit::petrinets::2::net_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::2::Net)


def test_lit::petrinets::2::net_constructor_exists():
    assert callable(lit::petriNets::2::Net.__init__)


def test_lit::petrinets::2::net_constructor_args():
    sig = inspect.signature(lit::petriNets::2::Net.__init__)
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
lit::petriNets::2::Arc_strategy = st.builds(
    lit::petriNets::2::Arc,
)
lit::petriNets::2::Transition_strategy = st.builds(
    lit::petriNets::2::Transition,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
lit::petriNets::2::TPArc_strategy = st.builds(
    lit::petriNets::2::TPArc,
)
lit::petriNets::2::PTArc_strategy = st.builds(
    lit::petriNets::2::PTArc,
)
lit::petriNets::2::Place_strategy = st.builds(
    lit::petriNets::2::Place,
    name=
        safe_text
)
lit::petriNets::2::Net_strategy = st.builds(
    lit::petriNets::2::Net,
)

@given(instance=lit::petriNets::2::Arc_strategy)
@settings(max_examples=50)
def test_lit::petrinets::2::arc_instantiation(instance):
    assert isinstance(instance, lit::petriNets::2::Arc)

@given(instance=lit::petriNets::2::Transition_strategy)
@settings(max_examples=50)
def test_lit::petrinets::2::transition_instantiation(instance):
    assert isinstance(instance, lit::petriNets::2::Transition)

@given(instance=lit::petriNets::2::Transition_strategy)
def test_lit::petrinets::2::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lit::petriNets::2::Transition_strategy)
def test_lit::petrinets::2::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=lit::petriNets::2::TPArc_strategy)
@settings(max_examples=50)
def test_lit::petrinets::2::tparc_instantiation(instance):
    assert isinstance(instance, lit::petriNets::2::TPArc)

@given(instance=lit::petriNets::2::PTArc_strategy)
@settings(max_examples=50)
def test_lit::petrinets::2::ptarc_instantiation(instance):
    assert isinstance(instance, lit::petriNets::2::PTArc)

@given(instance=lit::petriNets::2::Place_strategy)
@settings(max_examples=50)
def test_lit::petrinets::2::place_instantiation(instance):
    assert isinstance(instance, lit::petriNets::2::Place)

@given(instance=lit::petriNets::2::Place_strategy)
def test_lit::petrinets::2::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lit::petriNets::2::Place_strategy)
def test_lit::petrinets::2::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit::petriNets::2::Net_strategy)
@settings(max_examples=50)
def test_lit::petrinets::2::net_instantiation(instance):
    assert isinstance(instance, lit::petriNets::2::Net)
