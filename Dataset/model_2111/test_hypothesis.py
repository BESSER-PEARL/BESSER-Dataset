import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TestMM2_Metadata,
    TestMM2_Test,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmm2_metadata_is_not_abstract():
    assert not inspect.isabstract(TestMM2_Metadata)


def test_testmm2_metadata_constructor_exists():
    assert callable(TestMM2_Metadata.__init__)


def test_testmm2_metadata_constructor_args():
    sig = inspect.signature(TestMM2_Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "webpage" in params, "Missing parameter 'webpage'"
    assert "user" in params, "Missing parameter 'user'"
    assert "taglist" in params, "Missing parameter 'taglist'"

def test_testmm2_metadata_has_date():
    assert hasattr(TestMM2_Metadata, "date")
    descriptor = None
    for klass in TestMM2_Metadata.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_testmm2_metadata_has_webpage():
    assert hasattr(TestMM2_Metadata, "webpage")
    descriptor = None
    for klass in TestMM2_Metadata.__mro__:
        if "webpage" in klass.__dict__:
            descriptor = klass.__dict__["webpage"]
            break
    assert isinstance(descriptor, property)

def test_testmm2_metadata_has_user():
    assert hasattr(TestMM2_Metadata, "user")
    descriptor = None
    for klass in TestMM2_Metadata.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_testmm2_metadata_has_taglist():
    assert hasattr(TestMM2_Metadata, "taglist")
    descriptor = None
    for klass in TestMM2_Metadata.__mro__:
        if "taglist" in klass.__dict__:
            descriptor = klass.__dict__["taglist"]
            break
    assert isinstance(descriptor, property)



def test_testmm2_test_is_not_abstract():
    assert not inspect.isabstract(TestMM2_Test)


def test_testmm2_test_constructor_exists():
    assert callable(TestMM2_Test.__init__)


def test_testmm2_test_constructor_args():
    sig = inspect.signature(TestMM2_Test.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_testmm2_test_has_id():
    assert hasattr(TestMM2_Test, "id")
    descriptor = None
    for klass in TestMM2_Test.__mro__:
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
TestMM2_Metadata_strategy = st.builds(
    TestMM2_Metadata,
    date=
        safe_text,
    webpage=
        safe_text,
    user=
        safe_text,
    taglist=
        safe_text
)
TestMM2_Test_strategy = st.builds(
    TestMM2_Test,
    id=
        safe_text
)

@given(instance=TestMM2_Metadata_strategy)
@settings(max_examples=50)
def test_testmm2_metadata_instantiation(instance):
    assert isinstance(instance, TestMM2_Metadata)



@given(instance=TestMM2_Metadata_strategy)
def test_testmm2_metadata_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=TestMM2_Metadata_strategy)
def test_testmm2_metadata_webpage_setter(instance):
    original = instance.webpage
    instance.webpage = original
    assert instance.webpage == original



@given(instance=TestMM2_Metadata_strategy)
def test_testmm2_metadata_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=TestMM2_Metadata_strategy)
def test_testmm2_metadata_taglist_setter(instance):
    original = instance.taglist
    instance.taglist = original
    assert instance.taglist == original

@given(instance=TestMM2_Test_strategy)
@settings(max_examples=50)
def test_testmm2_test_instantiation(instance):
    assert isinstance(instance, TestMM2_Test)



@given(instance=TestMM2_Test_strategy)
def test_testmm2_test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
