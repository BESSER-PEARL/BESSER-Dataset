import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    List_Element,
    List_List,
    SubTestPackage_List_Element,
    List_SubTestPackage_SubTest,
    TestPackage_List_Element,
    List_TestPackage_Test,
    SubTestPackage_SubTest,
    Test,
    listType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_list_element_is_not_abstract():
    assert not inspect.isabstract(List_Element)


def test_list_element_constructor_exists():
    assert callable(List_Element.__init__)


def test_list_element_constructor_args():
    sig = inspect.signature(List_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_list_element_has_name():
    assert hasattr(List_Element, "name")
    descriptor = None
    for klass in List_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_list_element_has_value():
    assert hasattr(List_Element, "value")
    descriptor = None
    for klass in List_Element.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_list_list_is_not_abstract():
    assert not inspect.isabstract(List_List)


def test_list_list_constructor_exists():
    assert callable(List_List.__init__)


def test_list_list_constructor_args():
    sig = inspect.signature(List_List.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "size" in params, "Missing parameter 'size'"

def test_list_list_has_type():
    assert hasattr(List_List, "type")
    descriptor = None
    for klass in List_List.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_list_list_has_size():
    assert hasattr(List_List, "size")
    descriptor = None
    for klass in List_List.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_subtestpackage_list_element_is_not_abstract():
    assert not inspect.isabstract(SubTestPackage_List_Element)


def test_subtestpackage_list_element_constructor_exists():
    assert callable(SubTestPackage_List_Element.__init__)


def test_subtestpackage_list_element_constructor_args():
    sig = inspect.signature(SubTestPackage_List_Element.__init__)
    params = list(sig.parameters.keys())



def test_list_subtestpackage_subtest_is_not_abstract():
    assert not inspect.isabstract(List_SubTestPackage_SubTest)


def test_list_subtestpackage_subtest_constructor_exists():
    assert callable(List_SubTestPackage_SubTest.__init__)


def test_list_subtestpackage_subtest_constructor_args():
    sig = inspect.signature(List_SubTestPackage_SubTest.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_list_subtestpackage_subtest_has_value():
    assert hasattr(List_SubTestPackage_SubTest, "value")
    descriptor = None
    for klass in List_SubTestPackage_SubTest.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_testpackage_list_element_is_not_abstract():
    assert not inspect.isabstract(TestPackage_List_Element)


def test_testpackage_list_element_constructor_exists():
    assert callable(TestPackage_List_Element.__init__)


def test_testpackage_list_element_constructor_args():
    sig = inspect.signature(TestPackage_List_Element.__init__)
    params = list(sig.parameters.keys())



def test_list_testpackage_test_is_not_abstract():
    assert not inspect.isabstract(List_TestPackage_Test)


def test_list_testpackage_test_constructor_exists():
    assert callable(List_TestPackage_Test.__init__)


def test_list_testpackage_test_constructor_args():
    sig = inspect.signature(List_TestPackage_Test.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_list_testpackage_test_has_value():
    assert hasattr(List_TestPackage_Test, "value")
    descriptor = None
    for klass in List_TestPackage_Test.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_subtestpackage_subtest_is_not_abstract():
    assert not inspect.isabstract(SubTestPackage_SubTest)


def test_subtestpackage_subtest_constructor_exists():
    assert callable(SubTestPackage_SubTest.__init__)


def test_subtestpackage_subtest_constructor_args():
    sig = inspect.signature(SubTestPackage_SubTest.__init__)
    params = list(sig.parameters.keys())



def test_test_is_not_abstract():
    assert not inspect.isabstract(Test)


def test_test_constructor_exists():
    assert callable(Test.__init__)


def test_test_constructor_args():
    sig = inspect.signature(Test.__init__)
    params = list(sig.parameters.keys())

def test_listtype_exists():
    # Check that the Enumeration exists
    assert listType is not None

def test_listtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in listType]
    expected_literals = [
        "List",
        "ArrayList",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in listType"


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
List_Element_strategy = st.builds(
    List_Element,
    name=
        safe_text,
    value=
        st.integers()
)
List_List_strategy = st.builds(
    List_List,
    type=
        safe_text,
    size=
        st.integers()
)
SubTestPackage_List_Element_strategy = st.builds(
    SubTestPackage_List_Element,
)
List_SubTestPackage_SubTest_strategy = st.builds(
    List_SubTestPackage_SubTest,
    value=
        st.integers()
)
TestPackage_List_Element_strategy = st.builds(
    TestPackage_List_Element,
)
List_TestPackage_Test_strategy = st.builds(
    List_TestPackage_Test,
    value=
        st.integers()
)
SubTestPackage_SubTest_strategy = st.builds(
    SubTestPackage_SubTest,
)
Test_strategy = st.builds(
    Test,
)

@given(instance=List_Element_strategy)
@settings(max_examples=50)
def test_list_element_instantiation(instance):
    assert isinstance(instance, List_Element)



@given(instance=List_Element_strategy)
def test_list_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=List_Element_strategy)
def test_list_element_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=List_List_strategy)
@settings(max_examples=50)
def test_list_list_instantiation(instance):
    assert isinstance(instance, List_List)



@given(instance=List_List_strategy)
def test_list_list_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=List_List_strategy)
def test_list_list_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=SubTestPackage_List_Element_strategy)
@settings(max_examples=50)
def test_subtestpackage_list_element_instantiation(instance):
    assert isinstance(instance, SubTestPackage_List_Element)

@given(instance=List_SubTestPackage_SubTest_strategy)
@settings(max_examples=50)
def test_list_subtestpackage_subtest_instantiation(instance):
    assert isinstance(instance, List_SubTestPackage_SubTest)



@given(instance=List_SubTestPackage_SubTest_strategy)
def test_list_subtestpackage_subtest_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TestPackage_List_Element_strategy)
@settings(max_examples=50)
def test_testpackage_list_element_instantiation(instance):
    assert isinstance(instance, TestPackage_List_Element)

@given(instance=List_TestPackage_Test_strategy)
@settings(max_examples=50)
def test_list_testpackage_test_instantiation(instance):
    assert isinstance(instance, List_TestPackage_Test)



@given(instance=List_TestPackage_Test_strategy)
def test_list_testpackage_test_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SubTestPackage_SubTest_strategy)
@settings(max_examples=50)
def test_subtestpackage_subtest_instantiation(instance):
    assert isinstance(instance, SubTestPackage_SubTest)

@given(instance=Test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, Test)
