import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ER_RelshipEnd,
    ER_ERAttribute,
    ER_Relship,
    ER_Entity,
    ER_ERSchema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_er_relshipend_is_not_abstract():
    assert not inspect.isabstract(ER_RelshipEnd)


def test_er_relshipend_constructor_exists():
    assert callable(ER_RelshipEnd.__init__)


def test_er_relshipend_constructor_args():
    sig = inspect.signature(ER_RelshipEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_relshipend_has_name():
    assert hasattr(ER_RelshipEnd, "name")
    descriptor = None
    for klass in ER_RelshipEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er_erattribute_is_not_abstract():
    assert not inspect.isabstract(ER_ERAttribute)


def test_er_erattribute_constructor_exists():
    assert callable(ER_ERAttribute.__init__)


def test_er_erattribute_constructor_args():
    sig = inspect.signature(ER_ERAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isKey" in params, "Missing parameter 'isKey'"

def test_er_erattribute_has_name():
    assert hasattr(ER_ERAttribute, "name")
    descriptor = None
    for klass in ER_ERAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_er_erattribute_has_isKey():
    assert hasattr(ER_ERAttribute, "isKey")
    descriptor = None
    for klass in ER_ERAttribute.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)



def test_er_relship_is_not_abstract():
    assert not inspect.isabstract(ER_Relship)


def test_er_relship_constructor_exists():
    assert callable(ER_Relship.__init__)


def test_er_relship_constructor_args():
    sig = inspect.signature(ER_Relship.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_relship_has_name():
    assert hasattr(ER_Relship, "name")
    descriptor = None
    for klass in ER_Relship.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er_entity_is_not_abstract():
    assert not inspect.isabstract(ER_Entity)


def test_er_entity_constructor_exists():
    assert callable(ER_Entity.__init__)


def test_er_entity_constructor_args():
    sig = inspect.signature(ER_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_entity_has_name():
    assert hasattr(ER_Entity, "name")
    descriptor = None
    for klass in ER_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er_erschema_is_not_abstract():
    assert not inspect.isabstract(ER_ERSchema)


def test_er_erschema_constructor_exists():
    assert callable(ER_ERSchema.__init__)


def test_er_erschema_constructor_args():
    sig = inspect.signature(ER_ERSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_erschema_has_name():
    assert hasattr(ER_ERSchema, "name")
    descriptor = None
    for klass in ER_ERSchema.__mro__:
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
ER_RelshipEnd_strategy = st.builds(
    ER_RelshipEnd,
    name=
        safe_text
)
ER_ERAttribute_strategy = st.builds(
    ER_ERAttribute,
    name=
        safe_text,
    isKey=
        st.booleans()
)
ER_Relship_strategy = st.builds(
    ER_Relship,
    name=
        safe_text
)
ER_Entity_strategy = st.builds(
    ER_Entity,
    name=
        safe_text
)
ER_ERSchema_strategy = st.builds(
    ER_ERSchema,
    name=
        safe_text
)

@given(instance=ER_RelshipEnd_strategy)
@settings(max_examples=50)
def test_er_relshipend_instantiation(instance):
    assert isinstance(instance, ER_RelshipEnd)



@given(instance=ER_RelshipEnd_strategy)
def test_er_relshipend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER_ERAttribute_strategy)
@settings(max_examples=50)
def test_er_erattribute_instantiation(instance):
    assert isinstance(instance, ER_ERAttribute)



@given(instance=ER_ERAttribute_strategy)
def test_er_erattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ER_ERAttribute_strategy)
def test_er_erattribute_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=ER_Relship_strategy)
@settings(max_examples=50)
def test_er_relship_instantiation(instance):
    assert isinstance(instance, ER_Relship)



@given(instance=ER_Relship_strategy)
def test_er_relship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER_Entity_strategy)
@settings(max_examples=50)
def test_er_entity_instantiation(instance):
    assert isinstance(instance, ER_Entity)



@given(instance=ER_Entity_strategy)
def test_er_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER_ERSchema_strategy)
@settings(max_examples=50)
def test_er_erschema_instantiation(instance):
    assert isinstance(instance, ER_ERSchema)



@given(instance=ER_ERSchema_strategy)
def test_er_erschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
