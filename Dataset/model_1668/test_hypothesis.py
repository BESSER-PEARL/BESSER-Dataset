import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hello121::Alias,
    hello121::NamedElement,
    hello121::Third,
    NamedElement,
    hello121::RelatedTo,
    hello121::Classoc,
    hello121::Thing,
    hello121::Base,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hello121::alias_is_not_abstract():
    assert not inspect.isabstract(hello121::Alias)


def test_hello121::alias_constructor_exists():
    assert callable(hello121::Alias.__init__)


def test_hello121::alias_constructor_args():
    sig = inspect.signature(hello121::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121::alias_has_id():
    assert hasattr(hello121::Alias, "id")
    descriptor = None
    for klass in hello121::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hello121::namedelement_is_not_abstract():
    assert not inspect.isabstract(hello121::NamedElement)


def test_hello121::namedelement_constructor_exists():
    assert callable(hello121::NamedElement.__init__)


def test_hello121::namedelement_constructor_args():
    sig = inspect.signature(hello121::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hello121::namedelement_has_name():
    assert hasattr(hello121::NamedElement, "name")
    descriptor = None
    for klass in hello121::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hello121::third_is_not_abstract():
    assert not inspect.isabstract(hello121::Third)


def test_hello121::third_constructor_exists():
    assert callable(hello121::Third.__init__)


def test_hello121::third_constructor_args():
    sig = inspect.signature(hello121::Third.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121::third_has_id():
    assert hasattr(hello121::Third, "id")
    descriptor = None
    for klass in hello121::Third.__mro__:
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



def test_hello121::relatedto_is_not_abstract():
    assert not inspect.isabstract(hello121::RelatedTo)


def test_hello121::relatedto_constructor_exists():
    assert callable(hello121::RelatedTo.__init__)


def test_hello121::relatedto_constructor_args():
    sig = inspect.signature(hello121::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_hello121::relatedto_has_since():
    assert hasattr(hello121::RelatedTo, "since")
    descriptor = None
    for klass in hello121::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_hello121::classoc_is_not_abstract():
    assert not inspect.isabstract(hello121::Classoc)


def test_hello121::classoc_constructor_exists():
    assert callable(hello121::Classoc.__init__)


def test_hello121::classoc_constructor_args():
    sig = inspect.signature(hello121::Classoc.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121::classoc_has_id():
    assert hasattr(hello121::Classoc, "id")
    descriptor = None
    for klass in hello121::Classoc.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hello121::thing_is_not_abstract():
    assert not inspect.isabstract(hello121::Thing)


def test_hello121::thing_constructor_exists():
    assert callable(hello121::Thing.__init__)


def test_hello121::thing_constructor_args():
    sig = inspect.signature(hello121::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hello121::thing_has_id():
    assert hasattr(hello121::Thing, "id")
    descriptor = None
    for klass in hello121::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hello121::base_is_not_abstract():
    assert not inspect.isabstract(hello121::Base)


def test_hello121::base_constructor_exists():
    assert callable(hello121::Base.__init__)


def test_hello121::base_constructor_args():
    sig = inspect.signature(hello121::Base.__init__)
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
hello121::Alias_strategy = st.builds(
    hello121::Alias,
    id=
        safe_text
)
hello121::NamedElement_strategy = st.builds(
    hello121::NamedElement,
    name=
        safe_text
)
hello121::Third_strategy = st.builds(
    hello121::Third,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hello121::RelatedTo_strategy = st.builds(
    hello121::RelatedTo,
    since=
        safe_text
)
hello121::Classoc_strategy = st.builds(
    hello121::Classoc,
    id=
        safe_text
)
hello121::Thing_strategy = st.builds(
    hello121::Thing,
    id=
        st.integers()
)
hello121::Base_strategy = st.builds(
    hello121::Base,
)

@given(instance=hello121::Alias_strategy)
@settings(max_examples=50)
def test_hello121::alias_instantiation(instance):
    assert isinstance(instance, hello121::Alias)

@given(instance=hello121::Alias_strategy)
def test_hello121::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=hello121::Alias_strategy)
def test_hello121::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hello121::NamedElement_strategy)
@settings(max_examples=50)
def test_hello121::namedelement_instantiation(instance):
    assert isinstance(instance, hello121::NamedElement)

@given(instance=hello121::NamedElement_strategy)
def test_hello121::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hello121::NamedElement_strategy)
def test_hello121::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hello121::Third_strategy)
@settings(max_examples=50)
def test_hello121::third_instantiation(instance):
    assert isinstance(instance, hello121::Third)

@given(instance=hello121::Third_strategy)
def test_hello121::third_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=hello121::Third_strategy)
def test_hello121::third_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hello121::RelatedTo_strategy)
@settings(max_examples=50)
def test_hello121::relatedto_instantiation(instance):
    assert isinstance(instance, hello121::RelatedTo)

@given(instance=hello121::RelatedTo_strategy)
def test_hello121::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=hello121::RelatedTo_strategy)
def test_hello121::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=hello121::Classoc_strategy)
@settings(max_examples=50)
def test_hello121::classoc_instantiation(instance):
    assert isinstance(instance, hello121::Classoc)

@given(instance=hello121::Classoc_strategy)
def test_hello121::classoc_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=hello121::Classoc_strategy)
def test_hello121::classoc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hello121::Thing_strategy)
@settings(max_examples=50)
def test_hello121::thing_instantiation(instance):
    assert isinstance(instance, hello121::Thing)

@given(instance=hello121::Thing_strategy)
def test_hello121::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=hello121::Thing_strategy)
def test_hello121::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hello121::Base_strategy)
@settings(max_examples=50)
def test_hello121::base_instantiation(instance):
    assert isinstance(instance, hello121::Base)
