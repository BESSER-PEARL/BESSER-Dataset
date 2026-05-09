import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    coom::Transition,
    coom::State,
    coom::Version,
    coom::ComponentOnOffManifest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coom::transition_is_not_abstract():
    assert not inspect.isabstract(coom::Transition)


def test_coom::transition_constructor_exists():
    assert callable(coom::Transition.__init__)


def test_coom::transition_constructor_args():
    sig = inspect.signature(coom::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_coom::transition_has_name():
    assert hasattr(coom::Transition, "name")
    descriptor = None
    for klass in coom::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_coom::state_is_not_abstract():
    assert not inspect.isabstract(coom::State)


def test_coom::state_constructor_exists():
    assert callable(coom::State.__init__)


def test_coom::state_constructor_args():
    sig = inspect.signature(coom::State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_coom::state_has_initial():
    assert hasattr(coom::State, "initial")
    descriptor = None
    for klass in coom::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_coom::state_has_name():
    assert hasattr(coom::State, "name")
    descriptor = None
    for klass in coom::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_coom::version_is_not_abstract():
    assert not inspect.isabstract(coom::Version)


def test_coom::version_constructor_exists():
    assert callable(coom::Version.__init__)


def test_coom::version_constructor_args():
    sig = inspect.signature(coom::Version.__init__)
    params = list(sig.parameters.keys())
    assert "minorValue" in params, "Missing parameter 'minorValue'"
    assert "majorMalue" in params, "Missing parameter 'majorMalue'"

def test_coom::version_has_minorValue():
    assert hasattr(coom::Version, "minorValue")
    descriptor = None
    for klass in coom::Version.__mro__:
        if "minorValue" in klass.__dict__:
            descriptor = klass.__dict__["minorValue"]
            break
    assert isinstance(descriptor, property)

def test_coom::version_has_majorMalue():
    assert hasattr(coom::Version, "majorMalue")
    descriptor = None
    for klass in coom::Version.__mro__:
        if "majorMalue" in klass.__dict__:
            descriptor = klass.__dict__["majorMalue"]
            break
    assert isinstance(descriptor, property)



def test_coom::componentonoffmanifest_is_not_abstract():
    assert not inspect.isabstract(coom::ComponentOnOffManifest)


def test_coom::componentonoffmanifest_constructor_exists():
    assert callable(coom::ComponentOnOffManifest.__init__)


def test_coom::componentonoffmanifest_constructor_args():
    sig = inspect.signature(coom::ComponentOnOffManifest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_coom::componentonoffmanifest_has_name():
    assert hasattr(coom::ComponentOnOffManifest, "name")
    descriptor = None
    for klass in coom::ComponentOnOffManifest.__mro__:
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
coom::Transition_strategy = st.builds(
    coom::Transition,
    name=
        safe_text
)
coom::State_strategy = st.builds(
    coom::State,
    initial=
        st.booleans(),
    name=
        safe_text
)
coom::Version_strategy = st.builds(
    coom::Version,
    minorValue=
        st.integers(),
    majorMalue=
        st.integers()
)
coom::ComponentOnOffManifest_strategy = st.builds(
    coom::ComponentOnOffManifest,
    name=
        safe_text
)

@given(instance=coom::Transition_strategy)
@settings(max_examples=50)
def test_coom::transition_instantiation(instance):
    assert isinstance(instance, coom::Transition)

@given(instance=coom::Transition_strategy)
def test_coom::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coom::Transition_strategy)
def test_coom::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coom::State_strategy)
@settings(max_examples=50)
def test_coom::state_instantiation(instance):
    assert isinstance(instance, coom::State)

@given(instance=coom::State_strategy)
def test_coom::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=coom::State_strategy)
def test_coom::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=coom::State_strategy)
def test_coom::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coom::State_strategy)
def test_coom::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coom::Version_strategy)
@settings(max_examples=50)
def test_coom::version_instantiation(instance):
    assert isinstance(instance, coom::Version)

@given(instance=coom::Version_strategy)
def test_coom::version_minorValue_type(instance):
    assert isinstance(instance.minorValue, int)


@given(instance=coom::Version_strategy)
def test_coom::version_minorValue_setter(instance):
    original = instance.minorValue
    instance.minorValue = original
    assert instance.minorValue == original

@given(instance=coom::Version_strategy)
def test_coom::version_majorMalue_type(instance):
    assert isinstance(instance.majorMalue, int)


@given(instance=coom::Version_strategy)
def test_coom::version_majorMalue_setter(instance):
    original = instance.majorMalue
    instance.majorMalue = original
    assert instance.majorMalue == original

@given(instance=coom::ComponentOnOffManifest_strategy)
@settings(max_examples=50)
def test_coom::componentonoffmanifest_instantiation(instance):
    assert isinstance(instance, coom::ComponentOnOffManifest)

@given(instance=coom::ComponentOnOffManifest_strategy)
def test_coom::componentonoffmanifest_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coom::ComponentOnOffManifest_strategy)
def test_coom::componentonoffmanifest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
