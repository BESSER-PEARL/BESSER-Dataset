import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ocldriven_Dependancy,
    ocldriven_Loans,
    ocldriven_Member,
    ocldriven_Media,
    ocldriven_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocldriven_dependancy_is_not_abstract():
    assert not inspect.isabstract(ocldriven_Dependancy)


def test_ocldriven_dependancy_constructor_exists():
    assert callable(ocldriven_Dependancy.__init__)


def test_ocldriven_dependancy_constructor_args():
    sig = inspect.signature(ocldriven_Dependancy.__init__)
    params = list(sig.parameters.keys())



def test_ocldriven_loans_is_not_abstract():
    assert not inspect.isabstract(ocldriven_Loans)


def test_ocldriven_loans_constructor_exists():
    assert callable(ocldriven_Loans.__init__)


def test_ocldriven_loans_constructor_args():
    sig = inspect.signature(ocldriven_Loans.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_ocldriven_loans_has_date():
    assert hasattr(ocldriven_Loans, "date")
    descriptor = None
    for klass in ocldriven_Loans.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_ocldriven_member_is_not_abstract():
    assert not inspect.isabstract(ocldriven_Member)


def test_ocldriven_member_constructor_exists():
    assert callable(ocldriven_Member.__init__)


def test_ocldriven_member_constructor_args():
    sig = inspect.signature(ocldriven_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocldriven_member_has_name():
    assert hasattr(ocldriven_Member, "name")
    descriptor = None
    for klass in ocldriven_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocldriven_media_is_not_abstract():
    assert not inspect.isabstract(ocldriven_Media)


def test_ocldriven_media_constructor_exists():
    assert callable(ocldriven_Media.__init__)


def test_ocldriven_media_constructor_args():
    sig = inspect.signature(ocldriven_Media.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "copies" in params, "Missing parameter 'copies'"

def test_ocldriven_media_has_name():
    assert hasattr(ocldriven_Media, "name")
    descriptor = None
    for klass in ocldriven_Media.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ocldriven_media_has_copies():
    assert hasattr(ocldriven_Media, "copies")
    descriptor = None
    for klass in ocldriven_Media.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_ocldriven_library_is_not_abstract():
    assert not inspect.isabstract(ocldriven_Library)


def test_ocldriven_library_constructor_exists():
    assert callable(ocldriven_Library.__init__)


def test_ocldriven_library_constructor_args():
    sig = inspect.signature(ocldriven_Library.__init__)
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
ocldriven_Dependancy_strategy = st.builds(
    ocldriven_Dependancy,
)
ocldriven_Loans_strategy = st.builds(
    ocldriven_Loans,
    date=
        st.dates()
)
ocldriven_Member_strategy = st.builds(
    ocldriven_Member,
    name=
        safe_text
)
ocldriven_Media_strategy = st.builds(
    ocldriven_Media,
    name=
        safe_text,
    copies=
        safe_text
)
ocldriven_Library_strategy = st.builds(
    ocldriven_Library,
)

@given(instance=ocldriven_Dependancy_strategy)
@settings(max_examples=50)
def test_ocldriven_dependancy_instantiation(instance):
    assert isinstance(instance, ocldriven_Dependancy)

@given(instance=ocldriven_Loans_strategy)
@settings(max_examples=50)
def test_ocldriven_loans_instantiation(instance):
    assert isinstance(instance, ocldriven_Loans)



@given(instance=ocldriven_Loans_strategy)
def test_ocldriven_loans_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=ocldriven_Member_strategy)
@settings(max_examples=50)
def test_ocldriven_member_instantiation(instance):
    assert isinstance(instance, ocldriven_Member)



@given(instance=ocldriven_Member_strategy)
def test_ocldriven_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocldriven_Media_strategy)
@settings(max_examples=50)
def test_ocldriven_media_instantiation(instance):
    assert isinstance(instance, ocldriven_Media)



@given(instance=ocldriven_Media_strategy)
def test_ocldriven_media_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ocldriven_Media_strategy)
def test_ocldriven_media_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=ocldriven_Library_strategy)
@settings(max_examples=50)
def test_ocldriven_library_instantiation(instance):
    assert isinstance(instance, ocldriven_Library)
