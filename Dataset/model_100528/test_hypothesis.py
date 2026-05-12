import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    useCase::Uses,
    useCase::Inheritance,
    useCase::ExtensionPoint,
    useCase::Case,
    useCase::Actor,
    useCase::Subsystem,
    useCase::UseCase,
    useCase::Extends,
    useCase::Includes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usecase::uses_is_not_abstract():
    assert not inspect.isabstract(useCase::Uses)


def test_usecase::uses_constructor_exists():
    assert callable(useCase::Uses.__init__)


def test_usecase::uses_constructor_args():
    sig = inspect.signature(useCase::Uses.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_usecase::uses_has_name():
    assert hasattr(useCase::Uses, "name")
    descriptor = None
    for klass in useCase::Uses.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_usecase::uses_has_multiplicity():
    assert hasattr(useCase::Uses, "multiplicity")
    descriptor = None
    for klass in useCase::Uses.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_usecase::inheritance_is_not_abstract():
    assert not inspect.isabstract(useCase::Inheritance)


def test_usecase::inheritance_constructor_exists():
    assert callable(useCase::Inheritance.__init__)


def test_usecase::inheritance_constructor_args():
    sig = inspect.signature(useCase::Inheritance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::inheritance_has_name():
    assert hasattr(useCase::Inheritance, "name")
    descriptor = None
    for klass in useCase::Inheritance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(useCase::ExtensionPoint)


def test_usecase::extensionpoint_constructor_exists():
    assert callable(useCase::ExtensionPoint.__init__)


def test_usecase::extensionpoint_constructor_args():
    sig = inspect.signature(useCase::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::extensionpoint_has_name():
    assert hasattr(useCase::ExtensionPoint, "name")
    descriptor = None
    for klass in useCase::ExtensionPoint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::case_is_not_abstract():
    assert not inspect.isabstract(useCase::Case)


def test_usecase::case_constructor_exists():
    assert callable(useCase::Case.__init__)


def test_usecase::case_constructor_args():
    sig = inspect.signature(useCase::Case.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::case_has_name():
    assert hasattr(useCase::Case, "name")
    descriptor = None
    for klass in useCase::Case.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::actor_is_not_abstract():
    assert not inspect.isabstract(useCase::Actor)


def test_usecase::actor_constructor_exists():
    assert callable(useCase::Actor.__init__)


def test_usecase::actor_constructor_args():
    sig = inspect.signature(useCase::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::actor_has_name():
    assert hasattr(useCase::Actor, "name")
    descriptor = None
    for klass in useCase::Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::subsystem_is_not_abstract():
    assert not inspect.isabstract(useCase::Subsystem)


def test_usecase::subsystem_constructor_exists():
    assert callable(useCase::Subsystem.__init__)


def test_usecase::subsystem_constructor_args():
    sig = inspect.signature(useCase::Subsystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::subsystem_has_name():
    assert hasattr(useCase::Subsystem, "name")
    descriptor = None
    for klass in useCase::Subsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::usecase_is_not_abstract():
    assert not inspect.isabstract(useCase::UseCase)


def test_usecase::usecase_constructor_exists():
    assert callable(useCase::UseCase.__init__)


def test_usecase::usecase_constructor_args():
    sig = inspect.signature(useCase::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase::extends_is_not_abstract():
    assert not inspect.isabstract(useCase::Extends)


def test_usecase::extends_constructor_exists():
    assert callable(useCase::Extends.__init__)


def test_usecase::extends_constructor_args():
    sig = inspect.signature(useCase::Extends.__init__)
    params = list(sig.parameters.keys())
    assert "rules" in params, "Missing parameter 'rules'"
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::extends_has_rules():
    assert hasattr(useCase::Extends, "rules")
    descriptor = None
    for klass in useCase::Extends.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)

def test_usecase::extends_has_name():
    assert hasattr(useCase::Extends, "name")
    descriptor = None
    for klass in useCase::Extends.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::includes_is_not_abstract():
    assert not inspect.isabstract(useCase::Includes)


def test_usecase::includes_constructor_exists():
    assert callable(useCase::Includes.__init__)


def test_usecase::includes_constructor_args():
    sig = inspect.signature(useCase::Includes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "rules" in params, "Missing parameter 'rules'"

def test_usecase::includes_has_name():
    assert hasattr(useCase::Includes, "name")
    descriptor = None
    for klass in useCase::Includes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_usecase::includes_has_rules():
    assert hasattr(useCase::Includes, "rules")
    descriptor = None
    for klass in useCase::Includes.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
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
useCase::Uses_strategy = st.builds(
    useCase::Uses,
    name=
        safe_text,
    multiplicity=
        safe_text
)
useCase::Inheritance_strategy = st.builds(
    useCase::Inheritance,
    name=
        safe_text
)
useCase::ExtensionPoint_strategy = st.builds(
    useCase::ExtensionPoint,
    name=
        safe_text
)
useCase::Case_strategy = st.builds(
    useCase::Case,
    name=
        safe_text
)
useCase::Actor_strategy = st.builds(
    useCase::Actor,
    name=
        safe_text
)
useCase::Subsystem_strategy = st.builds(
    useCase::Subsystem,
    name=
        safe_text
)
useCase::UseCase_strategy = st.builds(
    useCase::UseCase,
)
useCase::Extends_strategy = st.builds(
    useCase::Extends,
    rules=
        safe_text,
    name=
        safe_text
)
useCase::Includes_strategy = st.builds(
    useCase::Includes,
    name=
        safe_text,
    rules=
        safe_text
)

@given(instance=useCase::Uses_strategy)
@settings(max_examples=50)
def test_usecase::uses_instantiation(instance):
    assert isinstance(instance, useCase::Uses)

@given(instance=useCase::Uses_strategy)
def test_usecase::uses_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Uses_strategy)
def test_usecase::uses_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::Uses_strategy)
def test_usecase::uses_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=useCase::Uses_strategy)
def test_usecase::uses_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=useCase::Inheritance_strategy)
@settings(max_examples=50)
def test_usecase::inheritance_instantiation(instance):
    assert isinstance(instance, useCase::Inheritance)

@given(instance=useCase::Inheritance_strategy)
def test_usecase::inheritance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Inheritance_strategy)
def test_usecase::inheritance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_usecase::extensionpoint_instantiation(instance):
    assert isinstance(instance, useCase::ExtensionPoint)

@given(instance=useCase::ExtensionPoint_strategy)
def test_usecase::extensionpoint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::ExtensionPoint_strategy)
def test_usecase::extensionpoint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::Case_strategy)
@settings(max_examples=50)
def test_usecase::case_instantiation(instance):
    assert isinstance(instance, useCase::Case)

@given(instance=useCase::Case_strategy)
def test_usecase::case_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Case_strategy)
def test_usecase::case_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::Actor_strategy)
@settings(max_examples=50)
def test_usecase::actor_instantiation(instance):
    assert isinstance(instance, useCase::Actor)

@given(instance=useCase::Actor_strategy)
def test_usecase::actor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Actor_strategy)
def test_usecase::actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::Subsystem_strategy)
@settings(max_examples=50)
def test_usecase::subsystem_instantiation(instance):
    assert isinstance(instance, useCase::Subsystem)

@given(instance=useCase::Subsystem_strategy)
def test_usecase::subsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Subsystem_strategy)
def test_usecase::subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::UseCase_strategy)
@settings(max_examples=50)
def test_usecase::usecase_instantiation(instance):
    assert isinstance(instance, useCase::UseCase)

@given(instance=useCase::Extends_strategy)
@settings(max_examples=50)
def test_usecase::extends_instantiation(instance):
    assert isinstance(instance, useCase::Extends)

@given(instance=useCase::Extends_strategy)
def test_usecase::extends_rules_type(instance):
    assert isinstance(instance.rules, str)


@given(instance=useCase::Extends_strategy)
def test_usecase::extends_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=useCase::Extends_strategy)
def test_usecase::extends_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Extends_strategy)
def test_usecase::extends_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::Includes_strategy)
@settings(max_examples=50)
def test_usecase::includes_instantiation(instance):
    assert isinstance(instance, useCase::Includes)

@given(instance=useCase::Includes_strategy)
def test_usecase::includes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=useCase::Includes_strategy)
def test_usecase::includes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=useCase::Includes_strategy)
def test_usecase::includes_rules_type(instance):
    assert isinstance(instance.rules, str)


@given(instance=useCase::Includes_strategy)
def test_usecase::includes_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original
