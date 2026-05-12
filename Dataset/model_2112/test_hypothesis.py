import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TestMM1_Action,
    TestMM1_Test,
    ActionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmm1_action_is_not_abstract():
    assert not inspect.isabstract(TestMM1_Action)


def test_testmm1_action_constructor_exists():
    assert callable(TestMM1_Action.__init__)


def test_testmm1_action_constructor_args():
    sig = inspect.signature(TestMM1_Action.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "xpath" in params, "Missing parameter 'xpath'"
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_testmm1_action_has_description():
    assert hasattr(TestMM1_Action, "description")
    descriptor = None
    for klass in TestMM1_Action.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_testmm1_action_has_id():
    assert hasattr(TestMM1_Action, "id")
    descriptor = None
    for klass in TestMM1_Action.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_testmm1_action_has_xpath():
    assert hasattr(TestMM1_Action, "xpath")
    descriptor = None
    for klass in TestMM1_Action.__mro__:
        if "xpath" in klass.__dict__:
            descriptor = klass.__dict__["xpath"]
            break
    assert isinstance(descriptor, property)

def test_testmm1_action_has_value():
    assert hasattr(TestMM1_Action, "value")
    descriptor = None
    for klass in TestMM1_Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_testmm1_action_has_type():
    assert hasattr(TestMM1_Action, "type")
    descriptor = None
    for klass in TestMM1_Action.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_testmm1_test_is_not_abstract():
    assert not inspect.isabstract(TestMM1_Test)


def test_testmm1_test_constructor_exists():
    assert callable(TestMM1_Test.__init__)


def test_testmm1_test_constructor_args():
    sig = inspect.signature(TestMM1_Test.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_testmm1_test_has_id():
    assert hasattr(TestMM1_Test, "id")
    descriptor = None
    for klass in TestMM1_Test.__mro__:
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
        "comment",
        "copy",
        "click",
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
TestMM1_Action_strategy = st.builds(
    TestMM1_Action,
    description=
        safe_text,
    id=
        safe_text,
    xpath=
        safe_text,
    value=
        safe_text,
    type=
        safe_text
)
TestMM1_Test_strategy = st.builds(
    TestMM1_Test,
    id=
        safe_text
)

@given(instance=TestMM1_Action_strategy)
@settings(max_examples=50)
def test_testmm1_action_instantiation(instance):
    assert isinstance(instance, TestMM1_Action)



@given(instance=TestMM1_Action_strategy)
def test_testmm1_action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=TestMM1_Action_strategy)
def test_testmm1_action_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=TestMM1_Action_strategy)
def test_testmm1_action_xpath_setter(instance):
    original = instance.xpath
    instance.xpath = original
    assert instance.xpath == original



@given(instance=TestMM1_Action_strategy)
def test_testmm1_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=TestMM1_Action_strategy)
def test_testmm1_action_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TestMM1_Test_strategy)
@settings(max_examples=50)
def test_testmm1_test_instantiation(instance):
    assert isinstance(instance, TestMM1_Test)



@given(instance=TestMM1_Test_strategy)
def test_testmm1_test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
