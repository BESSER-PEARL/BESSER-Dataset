import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hello121_Alias,
    hello121_NamedElement,
    hello121_Third,
    NamedElement,
    hello121_RelatedTo,
    hello121_Classoc,
    hello121_Thing,
    hello121_Base,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hello121_alias_is_not_abstract():
    assert not inspect.isabstract(hello121_Alias)


def test_hello121_alias_constructor_exists():
    assert callable(hello121_Alias.__init__)


def test_hello121_alias_constructor_args():
    sig = inspect.signature(hello121_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121_alias_has_id():
    assert hasattr(hello121_Alias, "id")
    descriptor = None
    for klass in hello121_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hello121_namedelement_is_not_abstract():
    assert not inspect.isabstract(hello121_NamedElement)


def test_hello121_namedelement_constructor_exists():
    assert callable(hello121_NamedElement.__init__)


def test_hello121_namedelement_constructor_args():
    sig = inspect.signature(hello121_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hello121_namedelement_has_name():
    assert hasattr(hello121_NamedElement, "name")
    descriptor = None
    for klass in hello121_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hello121_third_is_not_abstract():
    assert not inspect.isabstract(hello121_Third)


def test_hello121_third_constructor_exists():
    assert callable(hello121_Third.__init__)


def test_hello121_third_constructor_args():
    sig = inspect.signature(hello121_Third.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121_third_has_id():
    assert hasattr(hello121_Third, "id")
    descriptor = None
    for klass in hello121_Third.__mro__:
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



def test_hello121_relatedto_is_not_abstract():
    assert not inspect.isabstract(hello121_RelatedTo)


def test_hello121_relatedto_constructor_exists():
    assert callable(hello121_RelatedTo.__init__)


def test_hello121_relatedto_constructor_args():
    sig = inspect.signature(hello121_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_hello121_relatedto_has_since():
    assert hasattr(hello121_RelatedTo, "since")
    descriptor = None
    for klass in hello121_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_hello121_classoc_is_not_abstract():
    assert not inspect.isabstract(hello121_Classoc)


def test_hello121_classoc_constructor_exists():
    assert callable(hello121_Classoc.__init__)


def test_hello121_classoc_constructor_args():
    sig = inspect.signature(hello121_Classoc.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121_classoc_has_id():
    assert hasattr(hello121_Classoc, "id")
    descriptor = None
    for klass in hello121_Classoc.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hello121_thing_is_not_abstract():
    assert not inspect.isabstract(hello121_Thing)


def test_hello121_thing_constructor_exists():
    assert callable(hello121_Thing.__init__)


def test_hello121_thing_constructor_args():
    sig = inspect.signature(hello121_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121_thing_has_id():
    assert hasattr(hello121_Thing, "id")
    descriptor = None
    for klass in hello121_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hello121_base_is_not_abstract():
    assert not inspect.isabstract(hello121_Base)


def test_hello121_base_constructor_exists():
    assert callable(hello121_Base.__init__)


def test_hello121_base_constructor_args():
    sig = inspect.signature(hello121_Base.__init__)
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
hello121_Alias_strategy = st.builds(
    hello121_Alias,
    id=
        safe_text
)
hello121_NamedElement_strategy = st.builds(
    hello121_NamedElement,
    name=
        safe_text
)
hello121_Third_strategy = st.builds(
    hello121_Third,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hello121_RelatedTo_strategy = st.builds(
    hello121_RelatedTo,
    since=
        safe_text
)
hello121_Classoc_strategy = st.builds(
    hello121_Classoc,
    id=
        safe_text
)
hello121_Thing_strategy = st.builds(
    hello121_Thing,
    id=
        st.integers()
)
hello121_Base_strategy = st.builds(
    hello121_Base,
)

@given(instance=hello121_Alias_strategy)
@settings(max_examples=50)
def test_hello121_alias_instantiation(instance):
    assert isinstance(instance, hello121_Alias)



@given(instance=hello121_Alias_strategy)
def test_hello121_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hello121_NamedElement_strategy)
@settings(max_examples=50)
def test_hello121_namedelement_instantiation(instance):
    assert isinstance(instance, hello121_NamedElement)



@given(instance=hello121_NamedElement_strategy)
def test_hello121_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hello121_Third_strategy)
@settings(max_examples=50)
def test_hello121_third_instantiation(instance):
    assert isinstance(instance, hello121_Third)



@given(instance=hello121_Third_strategy)
def test_hello121_third_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hello121_RelatedTo_strategy)
@settings(max_examples=50)
def test_hello121_relatedto_instantiation(instance):
    assert isinstance(instance, hello121_RelatedTo)



@given(instance=hello121_RelatedTo_strategy)
def test_hello121_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=hello121_Classoc_strategy)
@settings(max_examples=50)
def test_hello121_classoc_instantiation(instance):
    assert isinstance(instance, hello121_Classoc)



@given(instance=hello121_Classoc_strategy)
def test_hello121_classoc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hello121_Thing_strategy)
@settings(max_examples=50)
def test_hello121_thing_instantiation(instance):
    assert isinstance(instance, hello121_Thing)



@given(instance=hello121_Thing_strategy)
def test_hello121_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hello121_Base_strategy)
@settings(max_examples=50)
def test_hello121_base_instantiation(instance):
    assert isinstance(instance, hello121_Base)
