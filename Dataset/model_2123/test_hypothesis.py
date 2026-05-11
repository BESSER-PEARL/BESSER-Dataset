import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    List::Element,
    List::List,
    SubTestPackage::List::Element,
    List::SubTestPackage::SubTest,
    TestPackage::List::Element,
    List::TestPackage::Test,
    SubTestPackage::SubTest,
    Test,
    listType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_list::element_is_not_abstract():
    assert not inspect.isabstract(List::Element)


def test_list::element_constructor_exists():
    assert callable(List::Element.__init__)


def test_list::element_constructor_args():
    sig = inspect.signature(List::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_list::element_has_name():
    assert hasattr(List::Element, "name")
    descriptor = None
    for klass in List::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_list::element_has_value():
    assert hasattr(List::Element, "value")
    descriptor = None
    for klass in List::Element.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_list::list_is_not_abstract():
    assert not inspect.isabstract(List::List)


def test_list::list_constructor_exists():
    assert callable(List::List.__init__)


def test_list::list_constructor_args():
    sig = inspect.signature(List::List.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "size" in params, "Missing parameter 'size'"

def test_list::list_has_type():
    assert hasattr(List::List, "type")
    descriptor = None
    for klass in List::List.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_list::list_has_size():
    assert hasattr(List::List, "size")
    descriptor = None
    for klass in List::List.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_subtestpackage::list::element_is_not_abstract():
    assert not inspect.isabstract(SubTestPackage::List::Element)


def test_subtestpackage::list::element_constructor_exists():
    assert callable(SubTestPackage::List::Element.__init__)


def test_subtestpackage::list::element_constructor_args():
    sig = inspect.signature(SubTestPackage::List::Element.__init__)
    params = list(sig.parameters.keys())



def test_list::subtestpackage::subtest_is_not_abstract():
    assert not inspect.isabstract(List::SubTestPackage::SubTest)


def test_list::subtestpackage::subtest_constructor_exists():
    assert callable(List::SubTestPackage::SubTest.__init__)


def test_list::subtestpackage::subtest_constructor_args():
    sig = inspect.signature(List::SubTestPackage::SubTest.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_list::subtestpackage::subtest_has_value():
    assert hasattr(List::SubTestPackage::SubTest, "value")
    descriptor = None
    for klass in List::SubTestPackage::SubTest.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_testpackage::list::element_is_not_abstract():
    assert not inspect.isabstract(TestPackage::List::Element)


def test_testpackage::list::element_constructor_exists():
    assert callable(TestPackage::List::Element.__init__)


def test_testpackage::list::element_constructor_args():
    sig = inspect.signature(TestPackage::List::Element.__init__)
    params = list(sig.parameters.keys())



def test_list::testpackage::test_is_not_abstract():
    assert not inspect.isabstract(List::TestPackage::Test)


def test_list::testpackage::test_constructor_exists():
    assert callable(List::TestPackage::Test.__init__)


def test_list::testpackage::test_constructor_args():
    sig = inspect.signature(List::TestPackage::Test.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_list::testpackage::test_has_value():
    assert hasattr(List::TestPackage::Test, "value")
    descriptor = None
    for klass in List::TestPackage::Test.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_subtestpackage::subtest_is_not_abstract():
    assert not inspect.isabstract(SubTestPackage::SubTest)


def test_subtestpackage::subtest_constructor_exists():
    assert callable(SubTestPackage::SubTest.__init__)


def test_subtestpackage::subtest_constructor_args():
    sig = inspect.signature(SubTestPackage::SubTest.__init__)
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
        "ArrayList",
        "List",
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
List::Element_strategy = st.builds(
    List::Element,
    name=
        safe_text,
    value=
        st.integers()
)
List::List_strategy = st.builds(
    List::List,
    type=
        safe_text,
    size=
        st.integers()
)
SubTestPackage::List::Element_strategy = st.builds(
    SubTestPackage::List::Element,
)
List::SubTestPackage::SubTest_strategy = st.builds(
    List::SubTestPackage::SubTest,
    value=
        st.integers()
)
TestPackage::List::Element_strategy = st.builds(
    TestPackage::List::Element,
)
List::TestPackage::Test_strategy = st.builds(
    List::TestPackage::Test,
    value=
        st.integers()
)
SubTestPackage::SubTest_strategy = st.builds(
    SubTestPackage::SubTest,
)
Test_strategy = st.builds(
    Test,
)

@given(instance=List::Element_strategy)
@settings(max_examples=50)
def test_list::element_instantiation(instance):
    assert isinstance(instance, List::Element)

@given(instance=List::Element_strategy)
def test_list::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=List::Element_strategy)
def test_list::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=List::Element_strategy)
def test_list::element_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=List::Element_strategy)
def test_list::element_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=List::List_strategy)
@settings(max_examples=50)
def test_list::list_instantiation(instance):
    assert isinstance(instance, List::List)

@given(instance=List::List_strategy)
def test_list::list_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=List::List_strategy)
def test_list::list_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=List::List_strategy)
def test_list::list_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=List::List_strategy)
def test_list::list_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=SubTestPackage::List::Element_strategy)
@settings(max_examples=50)
def test_subtestpackage::list::element_instantiation(instance):
    assert isinstance(instance, SubTestPackage::List::Element)

@given(instance=List::SubTestPackage::SubTest_strategy)
@settings(max_examples=50)
def test_list::subtestpackage::subtest_instantiation(instance):
    assert isinstance(instance, List::SubTestPackage::SubTest)

@given(instance=List::SubTestPackage::SubTest_strategy)
def test_list::subtestpackage::subtest_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=List::SubTestPackage::SubTest_strategy)
def test_list::subtestpackage::subtest_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TestPackage::List::Element_strategy)
@settings(max_examples=50)
def test_testpackage::list::element_instantiation(instance):
    assert isinstance(instance, TestPackage::List::Element)

@given(instance=List::TestPackage::Test_strategy)
@settings(max_examples=50)
def test_list::testpackage::test_instantiation(instance):
    assert isinstance(instance, List::TestPackage::Test)

@given(instance=List::TestPackage::Test_strategy)
def test_list::testpackage::test_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=List::TestPackage::Test_strategy)
def test_list::testpackage::test_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SubTestPackage::SubTest_strategy)
@settings(max_examples=50)
def test_subtestpackage::subtest_instantiation(instance):
    assert isinstance(instance, SubTestPackage::SubTest)

@given(instance=Test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, Test)
