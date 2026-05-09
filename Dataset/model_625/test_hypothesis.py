import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocldriven::Dependancy,
    ocldriven::Loans,
    ocldriven::Member,
    ocldriven::Media,
    ocldriven::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocldriven::dependancy_is_not_abstract():
    assert not inspect.isabstract(ocldriven::Dependancy)


def test_ocldriven::dependancy_constructor_exists():
    assert callable(ocldriven::Dependancy.__init__)


def test_ocldriven::dependancy_constructor_args():
    sig = inspect.signature(ocldriven::Dependancy.__init__)
    params = list(sig.parameters.keys())



def test_ocldriven::loans_is_not_abstract():
    assert not inspect.isabstract(ocldriven::Loans)


def test_ocldriven::loans_constructor_exists():
    assert callable(ocldriven::Loans.__init__)


def test_ocldriven::loans_constructor_args():
    sig = inspect.signature(ocldriven::Loans.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_ocldriven::loans_has_date():
    assert hasattr(ocldriven::Loans, "date")
    descriptor = None
    for klass in ocldriven::Loans.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_ocldriven::member_is_not_abstract():
    assert not inspect.isabstract(ocldriven::Member)


def test_ocldriven::member_constructor_exists():
    assert callable(ocldriven::Member.__init__)


def test_ocldriven::member_constructor_args():
    sig = inspect.signature(ocldriven::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocldriven::member_has_name():
    assert hasattr(ocldriven::Member, "name")
    descriptor = None
    for klass in ocldriven::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocldriven::media_is_not_abstract():
    assert not inspect.isabstract(ocldriven::Media)


def test_ocldriven::media_constructor_exists():
    assert callable(ocldriven::Media.__init__)


def test_ocldriven::media_constructor_args():
    sig = inspect.signature(ocldriven::Media.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocldriven::media_has_copies():
    assert hasattr(ocldriven::Media, "copies")
    descriptor = None
    for klass in ocldriven::Media.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)

def test_ocldriven::media_has_name():
    assert hasattr(ocldriven::Media, "name")
    descriptor = None
    for klass in ocldriven::Media.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocldriven::library_is_not_abstract():
    assert not inspect.isabstract(ocldriven::Library)


def test_ocldriven::library_constructor_exists():
    assert callable(ocldriven::Library.__init__)


def test_ocldriven::library_constructor_args():
    sig = inspect.signature(ocldriven::Library.__init__)
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
ocldriven::Dependancy_strategy = st.builds(
    ocldriven::Dependancy,
)
ocldriven::Loans_strategy = st.builds(
    ocldriven::Loans,
    date=
        st.dates()
)
ocldriven::Member_strategy = st.builds(
    ocldriven::Member,
    name=
        safe_text
)
ocldriven::Media_strategy = st.builds(
    ocldriven::Media,
    copies=
        safe_text,
    name=
        safe_text
)
ocldriven::Library_strategy = st.builds(
    ocldriven::Library,
)

@given(instance=ocldriven::Dependancy_strategy)
@settings(max_examples=50)
def test_ocldriven::dependancy_instantiation(instance):
    assert isinstance(instance, ocldriven::Dependancy)

@given(instance=ocldriven::Loans_strategy)
@settings(max_examples=50)
def test_ocldriven::loans_instantiation(instance):
    assert isinstance(instance, ocldriven::Loans)

@given(instance=ocldriven::Loans_strategy)
def test_ocldriven::loans_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=ocldriven::Loans_strategy)
def test_ocldriven::loans_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=ocldriven::Member_strategy)
@settings(max_examples=50)
def test_ocldriven::member_instantiation(instance):
    assert isinstance(instance, ocldriven::Member)

@given(instance=ocldriven::Member_strategy)
def test_ocldriven::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocldriven::Member_strategy)
def test_ocldriven::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocldriven::Media_strategy)
@settings(max_examples=50)
def test_ocldriven::media_instantiation(instance):
    assert isinstance(instance, ocldriven::Media)

@given(instance=ocldriven::Media_strategy)
def test_ocldriven::media_copies_type(instance):
    assert isinstance(instance.copies, str)


@given(instance=ocldriven::Media_strategy)
def test_ocldriven::media_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=ocldriven::Media_strategy)
def test_ocldriven::media_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocldriven::Media_strategy)
def test_ocldriven::media_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocldriven::Library_strategy)
@settings(max_examples=50)
def test_ocldriven::library_instantiation(instance):
    assert isinstance(instance, ocldriven::Library)
