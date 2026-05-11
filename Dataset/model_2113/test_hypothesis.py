import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TestMM::Action,
    TestMM::Metadata,
    TestMM::Test,
    ActionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmm::action_is_not_abstract():
    assert not inspect.isabstract(TestMM::Action)


def test_testmm::action_constructor_exists():
    assert callable(TestMM::Action.__init__)


def test_testmm::action_constructor_args():
    sig = inspect.signature(TestMM::Action.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"
    assert "xpath" in params, "Missing parameter 'xpath'"

def test_testmm::action_has_description():
    assert hasattr(TestMM::Action, "description")
    descriptor = None
    for klass in TestMM::Action.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_testmm::action_has_type():
    assert hasattr(TestMM::Action, "type")
    descriptor = None
    for klass in TestMM::Action.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_testmm::action_has_value():
    assert hasattr(TestMM::Action, "value")
    descriptor = None
    for klass in TestMM::Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_testmm::action_has_id():
    assert hasattr(TestMM::Action, "id")
    descriptor = None
    for klass in TestMM::Action.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_testmm::action_has_xpath():
    assert hasattr(TestMM::Action, "xpath")
    descriptor = None
    for klass in TestMM::Action.__mro__:
        if "xpath" in klass.__dict__:
            descriptor = klass.__dict__["xpath"]
            break
    assert isinstance(descriptor, property)



def test_testmm::metadata_is_not_abstract():
    assert not inspect.isabstract(TestMM::Metadata)


def test_testmm::metadata_constructor_exists():
    assert callable(TestMM::Metadata.__init__)


def test_testmm::metadata_constructor_args():
    sig = inspect.signature(TestMM::Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "webpage" in params, "Missing parameter 'webpage'"
    assert "user" in params, "Missing parameter 'user'"
    assert "taglist" in params, "Missing parameter 'taglist'"
    assert "date" in params, "Missing parameter 'date'"

def test_testmm::metadata_has_webpage():
    assert hasattr(TestMM::Metadata, "webpage")
    descriptor = None
    for klass in TestMM::Metadata.__mro__:
        if "webpage" in klass.__dict__:
            descriptor = klass.__dict__["webpage"]
            break
    assert isinstance(descriptor, property)

def test_testmm::metadata_has_user():
    assert hasattr(TestMM::Metadata, "user")
    descriptor = None
    for klass in TestMM::Metadata.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_testmm::metadata_has_taglist():
    assert hasattr(TestMM::Metadata, "taglist")
    descriptor = None
    for klass in TestMM::Metadata.__mro__:
        if "taglist" in klass.__dict__:
            descriptor = klass.__dict__["taglist"]
            break
    assert isinstance(descriptor, property)

def test_testmm::metadata_has_date():
    assert hasattr(TestMM::Metadata, "date")
    descriptor = None
    for klass in TestMM::Metadata.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_testmm::test_is_not_abstract():
    assert not inspect.isabstract(TestMM::Test)


def test_testmm::test_constructor_exists():
    assert callable(TestMM::Test.__init__)


def test_testmm::test_constructor_args():
    sig = inspect.signature(TestMM::Test.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_testmm::test_has_id():
    assert hasattr(TestMM::Test, "id")
    descriptor = None
    for klass in TestMM::Test.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_actiontype_exists():
    # Check that the Enumeration exists
    assert ActionType is not None

def test_actiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionType]
    expected_literals = [
        "click",
        "insert",
        "comment",
        "copy",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionType"


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
TestMM::Action_strategy = st.builds(
    TestMM::Action,
    description=
        safe_text,
    type=
        safe_text,
    value=
        safe_text,
    id=
        safe_text,
    xpath=
        safe_text
)
TestMM::Metadata_strategy = st.builds(
    TestMM::Metadata,
    webpage=
        safe_text,
    user=
        safe_text,
    taglist=
        safe_text,
    date=
        safe_text
)
TestMM::Test_strategy = st.builds(
    TestMM::Test,
    id=
        safe_text
)

@given(instance=TestMM::Action_strategy)
@settings(max_examples=50)
def test_testmm::action_instantiation(instance):
    assert isinstance(instance, TestMM::Action)

@given(instance=TestMM::Action_strategy)
def test_testmm::action_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=TestMM::Action_strategy)
def test_testmm::action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=TestMM::Action_strategy)
def test_testmm::action_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=TestMM::Action_strategy)
def test_testmm::action_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TestMM::Action_strategy)
def test_testmm::action_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=TestMM::Action_strategy)
def test_testmm::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TestMM::Action_strategy)
def test_testmm::action_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=TestMM::Action_strategy)
def test_testmm::action_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TestMM::Action_strategy)
def test_testmm::action_xpath_type(instance):
    assert isinstance(instance.xpath, str)


@given(instance=TestMM::Action_strategy)
def test_testmm::action_xpath_setter(instance):
    original = instance.xpath
    instance.xpath = original
    assert instance.xpath == original

@given(instance=TestMM::Metadata_strategy)
@settings(max_examples=50)
def test_testmm::metadata_instantiation(instance):
    assert isinstance(instance, TestMM::Metadata)

@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_webpage_type(instance):
    assert isinstance(instance.webpage, str)


@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_webpage_setter(instance):
    original = instance.webpage
    instance.webpage = original
    assert instance.webpage == original

@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_taglist_type(instance):
    assert isinstance(instance.taglist, str)


@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_taglist_setter(instance):
    original = instance.taglist
    instance.taglist = original
    assert instance.taglist == original

@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=TestMM::Metadata_strategy)
def test_testmm::metadata_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=TestMM::Test_strategy)
@settings(max_examples=50)
def test_testmm::test_instantiation(instance):
    assert isinstance(instance, TestMM::Test)

@given(instance=TestMM::Test_strategy)
def test_testmm::test_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=TestMM::Test_strategy)
def test_testmm::test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
