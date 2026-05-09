import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    workbench101::NamedElement,
    NamedElement,
    workbench101::RelatedTo,
    workbench101::Thoughts,
    workbench101::Thing,
    workbench101::Workbench,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_workbench101::namedelement_is_not_abstract():
    assert not inspect.isabstract(workbench101::NamedElement)


def test_workbench101::namedelement_constructor_exists():
    assert callable(workbench101::NamedElement.__init__)


def test_workbench101::namedelement_constructor_args():
    sig = inspect.signature(workbench101::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workbench101::namedelement_has_name():
    assert hasattr(workbench101::NamedElement, "name")
    descriptor = None
    for klass in workbench101::NamedElement.__mro__:
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



def test_workbench101::relatedto_is_not_abstract():
    assert not inspect.isabstract(workbench101::RelatedTo)


def test_workbench101::relatedto_constructor_exists():
    assert callable(workbench101::RelatedTo.__init__)


def test_workbench101::relatedto_constructor_args():
    sig = inspect.signature(workbench101::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_workbench101::relatedto_has_since():
    assert hasattr(workbench101::RelatedTo, "since")
    descriptor = None
    for klass in workbench101::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_workbench101::thoughts_is_not_abstract():
    assert not inspect.isabstract(workbench101::Thoughts)


def test_workbench101::thoughts_constructor_exists():
    assert callable(workbench101::Thoughts.__init__)


def test_workbench101::thoughts_constructor_args():
    sig = inspect.signature(workbench101::Thoughts.__init__)
    params = list(sig.parameters.keys())



def test_workbench101::thing_is_not_abstract():
    assert not inspect.isabstract(workbench101::Thing)


def test_workbench101::thing_constructor_exists():
    assert callable(workbench101::Thing.__init__)


def test_workbench101::thing_constructor_args():
    sig = inspect.signature(workbench101::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_workbench101::thing_has_id():
    assert hasattr(workbench101::Thing, "id")
    descriptor = None
    for klass in workbench101::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_workbench101::workbench_is_not_abstract():
    assert not inspect.isabstract(workbench101::Workbench)


def test_workbench101::workbench_constructor_exists():
    assert callable(workbench101::Workbench.__init__)


def test_workbench101::workbench_constructor_args():
    sig = inspect.signature(workbench101::Workbench.__init__)
    params = list(sig.parameters.keys())
    assert "aprop" in params, "Missing parameter 'aprop'"

def test_workbench101::workbench_has_aprop():
    assert hasattr(workbench101::Workbench, "aprop")
    descriptor = None
    for klass in workbench101::Workbench.__mro__:
        if "aprop" in klass.__dict__:
            descriptor = klass.__dict__["aprop"]
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
workbench101::NamedElement_strategy = st.builds(
    workbench101::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
workbench101::RelatedTo_strategy = st.builds(
    workbench101::RelatedTo,
    since=
        safe_text
)
workbench101::Thoughts_strategy = st.builds(
    workbench101::Thoughts,
)
workbench101::Thing_strategy = st.builds(
    workbench101::Thing,
    id=
        st.integers()
)
workbench101::Workbench_strategy = st.builds(
    workbench101::Workbench,
    aprop=
        safe_text
)

@given(instance=workbench101::NamedElement_strategy)
@settings(max_examples=50)
def test_workbench101::namedelement_instantiation(instance):
    assert isinstance(instance, workbench101::NamedElement)

@given(instance=workbench101::NamedElement_strategy)
def test_workbench101::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workbench101::NamedElement_strategy)
def test_workbench101::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=workbench101::RelatedTo_strategy)
@settings(max_examples=50)
def test_workbench101::relatedto_instantiation(instance):
    assert isinstance(instance, workbench101::RelatedTo)

@given(instance=workbench101::RelatedTo_strategy)
def test_workbench101::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=workbench101::RelatedTo_strategy)
def test_workbench101::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=workbench101::Thoughts_strategy)
@settings(max_examples=50)
def test_workbench101::thoughts_instantiation(instance):
    assert isinstance(instance, workbench101::Thoughts)

@given(instance=workbench101::Thing_strategy)
@settings(max_examples=50)
def test_workbench101::thing_instantiation(instance):
    assert isinstance(instance, workbench101::Thing)

@given(instance=workbench101::Thing_strategy)
def test_workbench101::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=workbench101::Thing_strategy)
def test_workbench101::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=workbench101::Workbench_strategy)
@settings(max_examples=50)
def test_workbench101::workbench_instantiation(instance):
    assert isinstance(instance, workbench101::Workbench)

@given(instance=workbench101::Workbench_strategy)
def test_workbench101::workbench_aprop_type(instance):
    assert isinstance(instance.aprop, str)


@given(instance=workbench101::Workbench_strategy)
def test_workbench101::workbench_aprop_setter(instance):
    original = instance.aprop
    instance.aprop = original
    assert instance.aprop == original
