import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TestMM2::Metadata,
    TestMM2::Test,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmm2::metadata_is_not_abstract():
    assert not inspect.isabstract(TestMM2::Metadata)


def test_testmm2::metadata_constructor_exists():
    assert callable(TestMM2::Metadata.__init__)


def test_testmm2::metadata_constructor_args():
    sig = inspect.signature(TestMM2::Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "webpage" in params, "Missing parameter 'webpage'"
    assert "date" in params, "Missing parameter 'date'"
    assert "user" in params, "Missing parameter 'user'"
    assert "taglist" in params, "Missing parameter 'taglist'"

def test_testmm2::metadata_has_webpage():
    assert hasattr(TestMM2::Metadata, "webpage")
    descriptor = None
    for klass in TestMM2::Metadata.__mro__:
        if "webpage" in klass.__dict__:
            descriptor = klass.__dict__["webpage"]
            break
    assert isinstance(descriptor, property)

def test_testmm2::metadata_has_date():
    assert hasattr(TestMM2::Metadata, "date")
    descriptor = None
    for klass in TestMM2::Metadata.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_testmm2::metadata_has_user():
    assert hasattr(TestMM2::Metadata, "user")
    descriptor = None
    for klass in TestMM2::Metadata.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_testmm2::metadata_has_taglist():
    assert hasattr(TestMM2::Metadata, "taglist")
    descriptor = None
    for klass in TestMM2::Metadata.__mro__:
        if "taglist" in klass.__dict__:
            descriptor = klass.__dict__["taglist"]
            break
    assert isinstance(descriptor, property)



def test_testmm2::test_is_not_abstract():
    assert not inspect.isabstract(TestMM2::Test)


def test_testmm2::test_constructor_exists():
    assert callable(TestMM2::Test.__init__)


def test_testmm2::test_constructor_args():
    sig = inspect.signature(TestMM2::Test.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_testmm2::test_has_id():
    assert hasattr(TestMM2::Test, "id")
    descriptor = None
    for klass in TestMM2::Test.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
TestMM2::Metadata_strategy = st.builds(
    TestMM2::Metadata,
    webpage=
        safe_text,
    date=
        safe_text,
    user=
        safe_text,
    taglist=
        safe_text
)
TestMM2::Test_strategy = st.builds(
    TestMM2::Test,
    id=
        safe_text
)

@given(instance=TestMM2::Metadata_strategy)
@settings(max_examples=50)
def test_testmm2::metadata_instantiation(instance):
    assert isinstance(instance, TestMM2::Metadata)

@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_webpage_type(instance):
    assert isinstance(instance.webpage, str)


@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_webpage_setter(instance):
    original = instance.webpage
    instance.webpage = original
    assert instance.webpage == original

@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_taglist_type(instance):
    assert isinstance(instance.taglist, str)


@given(instance=TestMM2::Metadata_strategy)
def test_testmm2::metadata_taglist_setter(instance):
    original = instance.taglist
    instance.taglist = original
    assert instance.taglist == original

@given(instance=TestMM2::Test_strategy)
@settings(max_examples=50)
def test_testmm2::test_instantiation(instance):
    assert isinstance(instance, TestMM2::Test)

@given(instance=TestMM2::Test_strategy)
def test_testmm2::test_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=TestMM2::Test_strategy)
def test_testmm2::test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
