import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    umlState::StateRule,
    umlState::Namespace,
    umlState::StateMachine,
    umlState::QualifiedName,
    umlState::ExitRule,
    umlState::DoRule,
    umlState::EntryRule,
    umlState::SubmachineRule,
    BehaviorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlstate::staterule_is_not_abstract():
    assert not inspect.isabstract(umlState::StateRule)


def test_umlstate::staterule_constructor_exists():
    assert callable(umlState::StateRule.__init__)


def test_umlstate::staterule_constructor_args():
    sig = inspect.signature(umlState::StateRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlstate::staterule_has_name():
    assert hasattr(umlState::StateRule, "name")
    descriptor = None
    for klass in umlState::StateRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlstate::namespace_is_not_abstract():
    assert not inspect.isabstract(umlState::Namespace)


def test_umlstate::namespace_constructor_exists():
    assert callable(umlState::Namespace.__init__)


def test_umlstate::namespace_constructor_args():
    sig = inspect.signature(umlState::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_umlstate::statemachine_is_not_abstract():
    assert not inspect.isabstract(umlState::StateMachine)


def test_umlstate::statemachine_constructor_exists():
    assert callable(umlState::StateMachine.__init__)


def test_umlstate::statemachine_constructor_args():
    sig = inspect.signature(umlState::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umlstate::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(umlState::QualifiedName)


def test_umlstate::qualifiedname_constructor_exists():
    assert callable(umlState::QualifiedName.__init__)


def test_umlstate::qualifiedname_constructor_args():
    sig = inspect.signature(umlState::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_umlstate::exitrule_is_not_abstract():
    assert not inspect.isabstract(umlState::ExitRule)


def test_umlstate::exitrule_constructor_exists():
    assert callable(umlState::ExitRule.__init__)


def test_umlstate::exitrule_constructor_args():
    sig = inspect.signature(umlState::ExitRule.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstate::exitrule_has_behaviorName():
    assert hasattr(umlState::ExitRule, "behaviorName")
    descriptor = None
    for klass in umlState::ExitRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)

def test_umlstate::exitrule_has_kind():
    assert hasattr(umlState::ExitRule, "kind")
    descriptor = None
    for klass in umlState::ExitRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstate::dorule_is_not_abstract():
    assert not inspect.isabstract(umlState::DoRule)


def test_umlstate::dorule_constructor_exists():
    assert callable(umlState::DoRule.__init__)


def test_umlstate::dorule_constructor_args():
    sig = inspect.signature(umlState::DoRule.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"

def test_umlstate::dorule_has_kind():
    assert hasattr(umlState::DoRule, "kind")
    descriptor = None
    for klass in umlState::DoRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlstate::dorule_has_behaviorName():
    assert hasattr(umlState::DoRule, "behaviorName")
    descriptor = None
    for klass in umlState::DoRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)



def test_umlstate::entryrule_is_not_abstract():
    assert not inspect.isabstract(umlState::EntryRule)


def test_umlstate::entryrule_constructor_exists():
    assert callable(umlState::EntryRule.__init__)


def test_umlstate::entryrule_constructor_args():
    sig = inspect.signature(umlState::EntryRule.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"

def test_umlstate::entryrule_has_kind():
    assert hasattr(umlState::EntryRule, "kind")
    descriptor = None
    for klass in umlState::EntryRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlstate::entryrule_has_behaviorName():
    assert hasattr(umlState::EntryRule, "behaviorName")
    descriptor = None
    for klass in umlState::EntryRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)



def test_umlstate::submachinerule_is_not_abstract():
    assert not inspect.isabstract(umlState::SubmachineRule)


def test_umlstate::submachinerule_constructor_exists():
    assert callable(umlState::SubmachineRule.__init__)


def test_umlstate::submachinerule_constructor_args():
    sig = inspect.signature(umlState::SubmachineRule.__init__)
    params = list(sig.parameters.keys())

def test_behaviorkind_exists():
    # Check that the Enumeration exists
    assert BehaviorKind is not None

def test_behaviorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BehaviorKind]
    expected_literals = [
        "OPAQUE_BEHAVIOR",
        "STATE_MACHINE",
        "ACTIVITY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BehaviorKind"


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
umlState::StateRule_strategy = st.builds(
    umlState::StateRule,
    name=
        safe_text
)
umlState::Namespace_strategy = st.builds(
    umlState::Namespace,
)
umlState::StateMachine_strategy = st.builds(
    umlState::StateMachine,
)
umlState::QualifiedName_strategy = st.builds(
    umlState::QualifiedName,
)
umlState::ExitRule_strategy = st.builds(
    umlState::ExitRule,
    behaviorName=
        safe_text,
    kind=
        safe_text
)
umlState::DoRule_strategy = st.builds(
    umlState::DoRule,
    kind=
        safe_text,
    behaviorName=
        safe_text
)
umlState::EntryRule_strategy = st.builds(
    umlState::EntryRule,
    kind=
        safe_text,
    behaviorName=
        safe_text
)
umlState::SubmachineRule_strategy = st.builds(
    umlState::SubmachineRule,
)

@given(instance=umlState::StateRule_strategy)
@settings(max_examples=50)
def test_umlstate::staterule_instantiation(instance):
    assert isinstance(instance, umlState::StateRule)

@given(instance=umlState::StateRule_strategy)
def test_umlstate::staterule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlState::StateRule_strategy)
def test_umlstate::staterule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlState::Namespace_strategy)
@settings(max_examples=50)
def test_umlstate::namespace_instantiation(instance):
    assert isinstance(instance, umlState::Namespace)

@given(instance=umlState::StateMachine_strategy)
@settings(max_examples=50)
def test_umlstate::statemachine_instantiation(instance):
    assert isinstance(instance, umlState::StateMachine)

@given(instance=umlState::QualifiedName_strategy)
@settings(max_examples=50)
def test_umlstate::qualifiedname_instantiation(instance):
    assert isinstance(instance, umlState::QualifiedName)

@given(instance=umlState::ExitRule_strategy)
@settings(max_examples=50)
def test_umlstate::exitrule_instantiation(instance):
    assert isinstance(instance, umlState::ExitRule)

@given(instance=umlState::ExitRule_strategy)
def test_umlstate::exitrule_behaviorName_type(instance):
    assert isinstance(instance.behaviorName, str)


@given(instance=umlState::ExitRule_strategy)
def test_umlstate::exitrule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original

@given(instance=umlState::ExitRule_strategy)
def test_umlstate::exitrule_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlState::ExitRule_strategy)
def test_umlstate::exitrule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlState::DoRule_strategy)
@settings(max_examples=50)
def test_umlstate::dorule_instantiation(instance):
    assert isinstance(instance, umlState::DoRule)

@given(instance=umlState::DoRule_strategy)
def test_umlstate::dorule_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlState::DoRule_strategy)
def test_umlstate::dorule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlState::DoRule_strategy)
def test_umlstate::dorule_behaviorName_type(instance):
    assert isinstance(instance.behaviorName, str)


@given(instance=umlState::DoRule_strategy)
def test_umlstate::dorule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original

@given(instance=umlState::EntryRule_strategy)
@settings(max_examples=50)
def test_umlstate::entryrule_instantiation(instance):
    assert isinstance(instance, umlState::EntryRule)

@given(instance=umlState::EntryRule_strategy)
def test_umlstate::entryrule_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlState::EntryRule_strategy)
def test_umlstate::entryrule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlState::EntryRule_strategy)
def test_umlstate::entryrule_behaviorName_type(instance):
    assert isinstance(instance.behaviorName, str)


@given(instance=umlState::EntryRule_strategy)
def test_umlstate::entryrule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original

@given(instance=umlState::SubmachineRule_strategy)
@settings(max_examples=50)
def test_umlstate::submachinerule_instantiation(instance):
    assert isinstance(instance, umlState::SubmachineRule)
