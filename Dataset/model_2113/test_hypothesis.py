import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TestMM_Action,
    TestMM_Metadata,
    TestMM_Test,
    ActionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmm_action_is_not_abstract():
    assert not inspect.isabstract(TestMM_Action)


def test_testmm_action_constructor_exists():
    assert callable(TestMM_Action.__init__)


def test_testmm_action_constructor_args():
    sig = inspect.signature(TestMM_Action.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "xpath" in params, "Missing parameter 'xpath'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_testmm_action_has_value():
    assert hasattr(TestMM_Action, "value")
    descriptor = None
    for klass in TestMM_Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_testmm_action_has_xpath():
    assert hasattr(TestMM_Action, "xpath")
    descriptor = None
    for klass in TestMM_Action.__mro__:
        if "xpath" in klass.__dict__:
            descriptor = klass.__dict__["xpath"]
            break
    assert isinstance(descriptor, property)

def test_testmm_action_has_type():
    assert hasattr(TestMM_Action, "type")
    descriptor = None
    for klass in TestMM_Action.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_testmm_action_has_description():
    assert hasattr(TestMM_Action, "description")
    descriptor = None
    for klass in TestMM_Action.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_testmm_action_has_id():
    assert hasattr(TestMM_Action, "id")
    descriptor = None
    for klass in TestMM_Action.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_testmm_metadata_is_not_abstract():
    assert not inspect.isabstract(TestMM_Metadata)


def test_testmm_metadata_constructor_exists():
    assert callable(TestMM_Metadata.__init__)


def test_testmm_metadata_constructor_args():
    sig = inspect.signature(TestMM_Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "user" in params, "Missing parameter 'user'"
    assert "taglist" in params, "Missing parameter 'taglist'"
    assert "webpage" in params, "Missing parameter 'webpage'"

def test_testmm_metadata_has_date():
    assert hasattr(TestMM_Metadata, "date")
    descriptor = None
    for klass in TestMM_Metadata.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_testmm_metadata_has_user():
    assert hasattr(TestMM_Metadata, "user")
    descriptor = None
    for klass in TestMM_Metadata.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_testmm_metadata_has_taglist():
    assert hasattr(TestMM_Metadata, "taglist")
    descriptor = None
    for klass in TestMM_Metadata.__mro__:
        if "taglist" in klass.__dict__:
            descriptor = klass.__dict__["taglist"]
            break
    assert isinstance(descriptor, property)

def test_testmm_metadata_has_webpage():
    assert hasattr(TestMM_Metadata, "webpage")
    descriptor = None
    for klass in TestMM_Metadata.__mro__:
        if "webpage" in klass.__dict__:
            descriptor = klass.__dict__["webpage"]
            break
    assert isinstance(descriptor, property)



def test_testmm_test_is_not_abstract():
    assert not inspect.isabstract(TestMM_Test)


def test_testmm_test_constructor_exists():
    assert callable(TestMM_Test.__init__)


def test_testmm_test_constructor_args():
    sig = inspect.signature(TestMM_Test.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_testmm_test_has_id():
    assert hasattr(TestMM_Test, "id")
    descriptor = None
    for klass in TestMM_Test.__mro__:
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
        "insert",
        "copy",
        "click",
        "comment",
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
TestMM_Action_strategy = st.builds(
    TestMM_Action,
    value=
        safe_text,
    xpath=
        safe_text,
    type=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
TestMM_Metadata_strategy = st.builds(
    TestMM_Metadata,
    date=
        safe_text,
    user=
        safe_text,
    taglist=
        safe_text,
    webpage=
        safe_text
)
TestMM_Test_strategy = st.builds(
    TestMM_Test,
    id=
        safe_text
)

@given(instance=TestMM_Action_strategy)
@settings(max_examples=50)
def test_testmm_action_instantiation(instance):
    assert isinstance(instance, TestMM_Action)



@given(instance=TestMM_Action_strategy)
def test_testmm_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=TestMM_Action_strategy)
def test_testmm_action_xpath_setter(instance):
    original = instance.xpath
    instance.xpath = original
    assert instance.xpath == original



@given(instance=TestMM_Action_strategy)
def test_testmm_action_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=TestMM_Action_strategy)
def test_testmm_action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=TestMM_Action_strategy)
def test_testmm_action_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=TestMM_Metadata_strategy)
@settings(max_examples=50)
def test_testmm_metadata_instantiation(instance):
    assert isinstance(instance, TestMM_Metadata)



@given(instance=TestMM_Metadata_strategy)
def test_testmm_metadata_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=TestMM_Metadata_strategy)
def test_testmm_metadata_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=TestMM_Metadata_strategy)
def test_testmm_metadata_taglist_setter(instance):
    original = instance.taglist
    instance.taglist = original
    assert instance.taglist == original



@given(instance=TestMM_Metadata_strategy)
def test_testmm_metadata_webpage_setter(instance):
    original = instance.webpage
    instance.webpage = original
    assert instance.webpage == original

@given(instance=TestMM_Test_strategy)
@settings(max_examples=50)
def test_testmm_test_instantiation(instance):
    assert isinstance(instance, TestMM_Test)



@given(instance=TestMM_Test_strategy)
def test_testmm_test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
