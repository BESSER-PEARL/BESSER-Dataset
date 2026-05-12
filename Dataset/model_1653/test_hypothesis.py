import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    errya_Alias,
    errya_NamedElement,
    NamedElement,
    errya_RelatedTo,
    errya_Thing,
    errya_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_errya_alias_is_not_abstract():
    assert not inspect.isabstract(errya_Alias)


def test_errya_alias_constructor_exists():
    assert callable(errya_Alias.__init__)


def test_errya_alias_constructor_args():
    sig = inspect.signature(errya_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_errya_alias_has_id():
    assert hasattr(errya_Alias, "id")
    descriptor = None
    for klass in errya_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_errya_namedelement_is_not_abstract():
    assert not inspect.isabstract(errya_NamedElement)


def test_errya_namedelement_constructor_exists():
    assert callable(errya_NamedElement.__init__)


def test_errya_namedelement_constructor_args():
    sig = inspect.signature(errya_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_errya_namedelement_has_name():
    assert hasattr(errya_NamedElement, "name")
    descriptor = None
    for klass in errya_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_errya_relatedto_is_not_abstract():
    assert not inspect.isabstract(errya_RelatedTo)


def test_errya_relatedto_constructor_exists():
    assert callable(errya_RelatedTo.__init__)


def test_errya_relatedto_constructor_args():
    sig = inspect.signature(errya_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_errya_relatedto_has_since():
    assert hasattr(errya_RelatedTo, "since")
    descriptor = None
    for klass in errya_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_errya_thing_is_not_abstract():
    assert not inspect.isabstract(errya_Thing)


def test_errya_thing_constructor_exists():
    assert callable(errya_Thing.__init__)


def test_errya_thing_constructor_args():
    sig = inspect.signature(errya_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_errya_thing_has_id():
    assert hasattr(errya_Thing, "id")
    descriptor = None
    for klass in errya_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_errya_world_is_not_abstract():
    assert not inspect.isabstract(errya_World)


def test_errya_world_constructor_exists():
    assert callable(errya_World.__init__)


def test_errya_world_constructor_args():
    sig = inspect.signature(errya_World.__init__)
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
errya_Alias_strategy = st.builds(
    errya_Alias,
    id=
        safe_text
)
errya_NamedElement_strategy = st.builds(
    errya_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
errya_RelatedTo_strategy = st.builds(
    errya_RelatedTo,
    since=
        safe_text
)
errya_Thing_strategy = st.builds(
    errya_Thing,
    id=
        st.integers()
)
errya_World_strategy = st.builds(
    errya_World,
)

@given(instance=errya_Alias_strategy)
@settings(max_examples=50)
def test_errya_alias_instantiation(instance):
    assert isinstance(instance, errya_Alias)



@given(instance=errya_Alias_strategy)
def test_errya_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=errya_NamedElement_strategy)
@settings(max_examples=50)
def test_errya_namedelement_instantiation(instance):
    assert isinstance(instance, errya_NamedElement)



@given(instance=errya_NamedElement_strategy)
def test_errya_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=errya_RelatedTo_strategy)
@settings(max_examples=50)
def test_errya_relatedto_instantiation(instance):
    assert isinstance(instance, errya_RelatedTo)



@given(instance=errya_RelatedTo_strategy)
def test_errya_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=errya_Thing_strategy)
@settings(max_examples=50)
def test_errya_thing_instantiation(instance):
    assert isinstance(instance, errya_Thing)



@given(instance=errya_Thing_strategy)
def test_errya_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=errya_World_strategy)
@settings(max_examples=50)
def test_errya_world_instantiation(instance):
    assert isinstance(instance, errya_World)
