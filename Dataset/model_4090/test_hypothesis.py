import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sihuhu::NamedElement,
    Rail,
    sihuhu::SwitchConnection,
    TrackElement,
    sihuhu::Switch,
    sihuhu::Rail,
    NamedElement,
    sihuhu::TrackElement,
    sihuhu::Train,
    sihuhu::Signal,
    sihuhu::Track,
    sihuhu::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sihuhu::namedelement_is_not_abstract():
    assert not inspect.isabstract(sihuhu::NamedElement)


def test_sihuhu::namedelement_constructor_exists():
    assert callable(sihuhu::NamedElement.__init__)


def test_sihuhu::namedelement_constructor_args():
    sig = inspect.signature(sihuhu::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sihuhu::namedelement_has_name():
    assert hasattr(sihuhu::NamedElement, "name")
    descriptor = None
    for klass in sihuhu::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rail_is_not_abstract():
    assert not inspect.isabstract(Rail)


def test_rail_constructor_exists():
    assert callable(Rail.__init__)


def test_rail_constructor_args():
    sig = inspect.signature(Rail.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::switchconnection_is_not_abstract():
    assert not inspect.isabstract(sihuhu::SwitchConnection)


def test_sihuhu::switchconnection_constructor_exists():
    assert callable(sihuhu::SwitchConnection.__init__)


def test_sihuhu::switchconnection_constructor_args():
    sig = inspect.signature(sihuhu::SwitchConnection.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(TrackElement)


def test_trackelement_constructor_exists():
    assert callable(TrackElement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::switch_is_not_abstract():
    assert not inspect.isabstract(sihuhu::Switch)


def test_sihuhu::switch_constructor_exists():
    assert callable(sihuhu::Switch.__init__)


def test_sihuhu::switch_constructor_args():
    sig = inspect.signature(sihuhu::Switch.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::rail_is_not_abstract():
    assert not inspect.isabstract(sihuhu::Rail)


def test_sihuhu::rail_constructor_exists():
    assert callable(sihuhu::Rail.__init__)


def test_sihuhu::rail_constructor_args():
    sig = inspect.signature(sihuhu::Rail.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::trackelement_is_not_abstract():
    assert not inspect.isabstract(sihuhu::TrackElement)


def test_sihuhu::trackelement_constructor_exists():
    assert callable(sihuhu::TrackElement.__init__)


def test_sihuhu::trackelement_constructor_args():
    sig = inspect.signature(sihuhu::TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::train_is_not_abstract():
    assert not inspect.isabstract(sihuhu::Train)


def test_sihuhu::train_constructor_exists():
    assert callable(sihuhu::Train.__init__)


def test_sihuhu::train_constructor_args():
    sig = inspect.signature(sihuhu::Train.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::signal_is_not_abstract():
    assert not inspect.isabstract(sihuhu::Signal)


def test_sihuhu::signal_constructor_exists():
    assert callable(sihuhu::Signal.__init__)


def test_sihuhu::signal_constructor_args():
    sig = inspect.signature(sihuhu::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_sihuhu::signal_has_enabled():
    assert hasattr(sihuhu::Signal, "enabled")
    descriptor = None
    for klass in sihuhu::Signal.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_sihuhu::track_is_not_abstract():
    assert not inspect.isabstract(sihuhu::Track)


def test_sihuhu::track_constructor_exists():
    assert callable(sihuhu::Track.__init__)


def test_sihuhu::track_constructor_args():
    sig = inspect.signature(sihuhu::Track.__init__)
    params = list(sig.parameters.keys())



def test_sihuhu::world_is_not_abstract():
    assert not inspect.isabstract(sihuhu::World)


def test_sihuhu::world_constructor_exists():
    assert callable(sihuhu::World.__init__)


def test_sihuhu::world_constructor_args():
    sig = inspect.signature(sihuhu::World.__init__)
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
sihuhu::NamedElement_strategy = st.builds(
    sihuhu::NamedElement,
    name=
        safe_text
)
Rail_strategy = st.builds(
    Rail,
)
sihuhu::SwitchConnection_strategy = st.builds(
    sihuhu::SwitchConnection,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
sihuhu::Switch_strategy = st.builds(
    sihuhu::Switch,
)
sihuhu::Rail_strategy = st.builds(
    sihuhu::Rail,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sihuhu::TrackElement_strategy = st.builds(
    sihuhu::TrackElement,
)
sihuhu::Train_strategy = st.builds(
    sihuhu::Train,
)
sihuhu::Signal_strategy = st.builds(
    sihuhu::Signal,
    enabled=
        st.booleans()
)
sihuhu::Track_strategy = st.builds(
    sihuhu::Track,
)
sihuhu::World_strategy = st.builds(
    sihuhu::World,
)

@given(instance=sihuhu::NamedElement_strategy)
@settings(max_examples=50)
def test_sihuhu::namedelement_instantiation(instance):
    assert isinstance(instance, sihuhu::NamedElement)

@given(instance=sihuhu::NamedElement_strategy)
def test_sihuhu::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sihuhu::NamedElement_strategy)
def test_sihuhu::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Rail_strategy)
@settings(max_examples=50)
def test_rail_instantiation(instance):
    assert isinstance(instance, Rail)

@given(instance=sihuhu::SwitchConnection_strategy)
@settings(max_examples=50)
def test_sihuhu::switchconnection_instantiation(instance):
    assert isinstance(instance, sihuhu::SwitchConnection)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=sihuhu::Switch_strategy)
@settings(max_examples=50)
def test_sihuhu::switch_instantiation(instance):
    assert isinstance(instance, sihuhu::Switch)

@given(instance=sihuhu::Rail_strategy)
@settings(max_examples=50)
def test_sihuhu::rail_instantiation(instance):
    assert isinstance(instance, sihuhu::Rail)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sihuhu::TrackElement_strategy)
@settings(max_examples=50)
def test_sihuhu::trackelement_instantiation(instance):
    assert isinstance(instance, sihuhu::TrackElement)

@given(instance=sihuhu::Train_strategy)
@settings(max_examples=50)
def test_sihuhu::train_instantiation(instance):
    assert isinstance(instance, sihuhu::Train)

@given(instance=sihuhu::Signal_strategy)
@settings(max_examples=50)
def test_sihuhu::signal_instantiation(instance):
    assert isinstance(instance, sihuhu::Signal)

@given(instance=sihuhu::Signal_strategy)
def test_sihuhu::signal_enabled_type(instance):
    assert isinstance(instance.enabled, bool)


@given(instance=sihuhu::Signal_strategy)
def test_sihuhu::signal_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=sihuhu::Track_strategy)
@settings(max_examples=50)
def test_sihuhu::track_instantiation(instance):
    assert isinstance(instance, sihuhu::Track)

@given(instance=sihuhu::World_strategy)
@settings(max_examples=50)
def test_sihuhu::world_instantiation(instance):
    assert isinstance(instance, sihuhu::World)
