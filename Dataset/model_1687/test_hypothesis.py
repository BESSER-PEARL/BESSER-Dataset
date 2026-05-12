import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yye_Foo,
    NamedElement,
    yye_Relation,
    yye_Base,
    yye_Alias,
    yye_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yye_foo_is_not_abstract():
    assert not inspect.isabstract(yye_Foo)


def test_yye_foo_constructor_exists():
    assert callable(yye_Foo.__init__)


def test_yye_foo_constructor_args():
    sig = inspect.signature(yye_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yye_foo_has_id():
    assert hasattr(yye_Foo, "id")
    descriptor = None
    for klass in yye_Foo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_yye_relation_is_not_abstract():
    assert not inspect.isabstract(yye_Relation)


def test_yye_relation_constructor_exists():
    assert callable(yye_Relation.__init__)


def test_yye_relation_constructor_args():
    sig = inspect.signature(yye_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yye_relation_has_since():
    assert hasattr(yye_Relation, "since")
    descriptor = None
    for klass in yye_Relation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yye_base_is_not_abstract():
    assert not inspect.isabstract(yye_Base)


def test_yye_base_constructor_exists():
    assert callable(yye_Base.__init__)


def test_yye_base_constructor_args():
    sig = inspect.signature(yye_Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yye_base_has_id():
    assert hasattr(yye_Base, "id")
    descriptor = None
    for klass in yye_Base.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yye_alias_is_not_abstract():
    assert not inspect.isabstract(yye_Alias)


def test_yye_alias_constructor_exists():
    assert callable(yye_Alias.__init__)


def test_yye_alias_constructor_args():
    sig = inspect.signature(yye_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yye_alias_has_id():
    assert hasattr(yye_Alias, "id")
    descriptor = None
    for klass in yye_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yye_namedelement_is_not_abstract():
    assert not inspect.isabstract(yye_NamedElement)


def test_yye_namedelement_constructor_exists():
    assert callable(yye_NamedElement.__init__)


def test_yye_namedelement_constructor_args():
    sig = inspect.signature(yye_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yye_namedelement_has_name():
    assert hasattr(yye_NamedElement, "name")
    descriptor = None
    for klass in yye_NamedElement.__mro__:
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
yye_Foo_strategy = st.builds(
    yye_Foo,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yye_Relation_strategy = st.builds(
    yye_Relation,
    since=
        safe_text
)
yye_Base_strategy = st.builds(
    yye_Base,
    id=
        st.integers()
)
yye_Alias_strategy = st.builds(
    yye_Alias,
    id=
        safe_text
)
yye_NamedElement_strategy = st.builds(
    yye_NamedElement,
    name=
        safe_text
)

@given(instance=yye_Foo_strategy)
@settings(max_examples=50)
def test_yye_foo_instantiation(instance):
    assert isinstance(instance, yye_Foo)



@given(instance=yye_Foo_strategy)
def test_yye_foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yye_Relation_strategy)
@settings(max_examples=50)
def test_yye_relation_instantiation(instance):
    assert isinstance(instance, yye_Relation)



@given(instance=yye_Relation_strategy)
def test_yye_relation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yye_Base_strategy)
@settings(max_examples=50)
def test_yye_base_instantiation(instance):
    assert isinstance(instance, yye_Base)



@given(instance=yye_Base_strategy)
def test_yye_base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yye_Alias_strategy)
@settings(max_examples=50)
def test_yye_alias_instantiation(instance):
    assert isinstance(instance, yye_Alias)



@given(instance=yye_Alias_strategy)
def test_yye_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yye_NamedElement_strategy)
@settings(max_examples=50)
def test_yye_namedelement_instantiation(instance):
    assert isinstance(instance, yye_NamedElement)



@given(instance=yye_NamedElement_strategy)
def test_yye_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
