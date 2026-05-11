import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ER::ERSchema,
    ER::RelshipEnd,
    ER::ERAttribute,
    ER::Relship,
    ER::Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_er::erschema_is_not_abstract():
    assert not inspect.isabstract(ER::ERSchema)


def test_er::erschema_constructor_exists():
    assert callable(ER::ERSchema.__init__)


def test_er::erschema_constructor_args():
    sig = inspect.signature(ER::ERSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::erschema_has_name():
    assert hasattr(ER::ERSchema, "name")
    descriptor = None
    for klass in ER::ERSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::relshipend_is_not_abstract():
    assert not inspect.isabstract(ER::RelshipEnd)


def test_er::relshipend_constructor_exists():
    assert callable(ER::RelshipEnd.__init__)


def test_er::relshipend_constructor_args():
    sig = inspect.signature(ER::RelshipEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::relshipend_has_name():
    assert hasattr(ER::RelshipEnd, "name")
    descriptor = None
    for klass in ER::RelshipEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::erattribute_is_not_abstract():
    assert not inspect.isabstract(ER::ERAttribute)


def test_er::erattribute_constructor_exists():
    assert callable(ER::ERAttribute.__init__)


def test_er::erattribute_constructor_args():
    sig = inspect.signature(ER::ERAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isKey" in params, "Missing parameter 'isKey'"
    assert "name" in params, "Missing parameter 'name'"

def test_er::erattribute_has_isKey():
    assert hasattr(ER::ERAttribute, "isKey")
    descriptor = None
    for klass in ER::ERAttribute.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)

def test_er::erattribute_has_name():
    assert hasattr(ER::ERAttribute, "name")
    descriptor = None
    for klass in ER::ERAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::relship_is_not_abstract():
    assert not inspect.isabstract(ER::Relship)


def test_er::relship_constructor_exists():
    assert callable(ER::Relship.__init__)


def test_er::relship_constructor_args():
    sig = inspect.signature(ER::Relship.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::relship_has_name():
    assert hasattr(ER::Relship, "name")
    descriptor = None
    for klass in ER::Relship.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::entity_is_not_abstract():
    assert not inspect.isabstract(ER::Entity)


def test_er::entity_constructor_exists():
    assert callable(ER::Entity.__init__)


def test_er::entity_constructor_args():
    sig = inspect.signature(ER::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::entity_has_name():
    assert hasattr(ER::Entity, "name")
    descriptor = None
    for klass in ER::Entity.__mro__:
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
ER::ERSchema_strategy = st.builds(
    ER::ERSchema,
    name=
        safe_text
)
ER::RelshipEnd_strategy = st.builds(
    ER::RelshipEnd,
    name=
        safe_text
)
ER::ERAttribute_strategy = st.builds(
    ER::ERAttribute,
    isKey=
        st.booleans(),
    name=
        safe_text
)
ER::Relship_strategy = st.builds(
    ER::Relship,
    name=
        safe_text
)
ER::Entity_strategy = st.builds(
    ER::Entity,
    name=
        safe_text
)

@given(instance=ER::ERSchema_strategy)
@settings(max_examples=50)
def test_er::erschema_instantiation(instance):
    assert isinstance(instance, ER::ERSchema)

@given(instance=ER::ERSchema_strategy)
def test_er::erschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::ERSchema_strategy)
def test_er::erschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::RelshipEnd_strategy)
@settings(max_examples=50)
def test_er::relshipend_instantiation(instance):
    assert isinstance(instance, ER::RelshipEnd)

@given(instance=ER::RelshipEnd_strategy)
def test_er::relshipend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::RelshipEnd_strategy)
def test_er::relshipend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::ERAttribute_strategy)
@settings(max_examples=50)
def test_er::erattribute_instantiation(instance):
    assert isinstance(instance, ER::ERAttribute)

@given(instance=ER::ERAttribute_strategy)
def test_er::erattribute_isKey_type(instance):
    assert isinstance(instance.isKey, bool)


@given(instance=ER::ERAttribute_strategy)
def test_er::erattribute_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=ER::ERAttribute_strategy)
def test_er::erattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::ERAttribute_strategy)
def test_er::erattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::Relship_strategy)
@settings(max_examples=50)
def test_er::relship_instantiation(instance):
    assert isinstance(instance, ER::Relship)

@given(instance=ER::Relship_strategy)
def test_er::relship_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::Relship_strategy)
def test_er::relship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::Entity_strategy)
@settings(max_examples=50)
def test_er::entity_instantiation(instance):
    assert isinstance(instance, ER::Entity)

@given(instance=ER::Entity_strategy)
def test_er::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::Entity_strategy)
def test_er::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
