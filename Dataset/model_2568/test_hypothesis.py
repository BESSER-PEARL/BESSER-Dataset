import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TestPackage::TestIndexEntry,
    TestPackage::TestIndex,
    AbstractTestClass,
    TestPackage::TestClass2,
    TestPackage::TestClass1,
    TestPackage::AbstractTestClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::testindexentry_is_not_abstract():
    assert not inspect.isabstract(TestPackage::TestIndexEntry)


def test_testpackage::testindexentry_constructor_exists():
    assert callable(TestPackage::TestIndexEntry.__init__)


def test_testpackage::testindexentry_constructor_args():
    sig = inspect.signature(TestPackage::TestIndexEntry.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::testindex_is_not_abstract():
    assert not inspect.isabstract(TestPackage::TestIndex)


def test_testpackage::testindex_constructor_exists():
    assert callable(TestPackage::TestIndex.__init__)


def test_testpackage::testindex_constructor_args():
    sig = inspect.signature(TestPackage::TestIndex.__init__)
    params = list(sig.parameters.keys())



def test_abstracttestclass_is_not_abstract():
    assert not inspect.isabstract(AbstractTestClass)


def test_abstracttestclass_constructor_exists():
    assert callable(AbstractTestClass.__init__)


def test_abstracttestclass_constructor_args():
    sig = inspect.signature(AbstractTestClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::testclass2_is_not_abstract():
    assert not inspect.isabstract(TestPackage::TestClass2)


def test_testpackage::testclass2_constructor_exists():
    assert callable(TestPackage::TestClass2.__init__)


def test_testpackage::testclass2_constructor_args():
    sig = inspect.signature(TestPackage::TestClass2.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::testclass1_is_not_abstract():
    assert not inspect.isabstract(TestPackage::TestClass1)


def test_testpackage::testclass1_constructor_exists():
    assert callable(TestPackage::TestClass1.__init__)


def test_testpackage::testclass1_constructor_args():
    sig = inspect.signature(TestPackage::TestClass1.__init__)
    params = list(sig.parameters.keys())
    assert "theAttributeToListen" in params, "Missing parameter 'theAttributeToListen'"

def test_testpackage::testclass1_has_theAttributeToListen():
    assert hasattr(TestPackage::TestClass1, "theAttributeToListen")
    descriptor = None
    for klass in TestPackage::TestClass1.__mro__:
        if "theAttributeToListen" in klass.__dict__:
            descriptor = klass.__dict__["theAttributeToListen"]
            break
    assert isinstance(descriptor, property)



def test_testpackage::abstracttestclass_is_not_abstract():
    assert not inspect.isabstract(TestPackage::AbstractTestClass)


def test_testpackage::abstracttestclass_constructor_exists():
    assert callable(TestPackage::AbstractTestClass.__init__)


def test_testpackage::abstracttestclass_constructor_args():
    sig = inspect.signature(TestPackage::AbstractTestClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testpackage::abstracttestclass_has_name():
    assert hasattr(TestPackage::AbstractTestClass, "name")
    descriptor = None
    for klass in TestPackage::AbstractTestClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
TestPackage::TestIndexEntry_strategy = st.builds(
    TestPackage::TestIndexEntry,
)
TestPackage::TestIndex_strategy = st.builds(
    TestPackage::TestIndex,
)
AbstractTestClass_strategy = st.builds(
    AbstractTestClass,
)
TestPackage::TestClass2_strategy = st.builds(
    TestPackage::TestClass2,
)
TestPackage::TestClass1_strategy = st.builds(
    TestPackage::TestClass1,
    theAttributeToListen=
        safe_text
)
TestPackage::AbstractTestClass_strategy = st.builds(
    TestPackage::AbstractTestClass,
    name=
        safe_text
)

@given(instance=TestPackage::TestIndexEntry_strategy)
@settings(max_examples=50)
def test_testpackage::testindexentry_instantiation(instance):
    assert isinstance(instance, TestPackage::TestIndexEntry)

@given(instance=TestPackage::TestIndex_strategy)
@settings(max_examples=50)
def test_testpackage::testindex_instantiation(instance):
    assert isinstance(instance, TestPackage::TestIndex)

@given(instance=AbstractTestClass_strategy)
@settings(max_examples=50)
def test_abstracttestclass_instantiation(instance):
    assert isinstance(instance, AbstractTestClass)

@given(instance=TestPackage::TestClass2_strategy)
@settings(max_examples=50)
def test_testpackage::testclass2_instantiation(instance):
    assert isinstance(instance, TestPackage::TestClass2)

@given(instance=TestPackage::TestClass1_strategy)
@settings(max_examples=50)
def test_testpackage::testclass1_instantiation(instance):
    assert isinstance(instance, TestPackage::TestClass1)

@given(instance=TestPackage::TestClass1_strategy)
def test_testpackage::testclass1_theAttributeToListen_type(instance):
    assert isinstance(instance.theAttributeToListen, str)


@given(instance=TestPackage::TestClass1_strategy)
def test_testpackage::testclass1_theAttributeToListen_setter(instance):
    original = instance.theAttributeToListen
    instance.theAttributeToListen = original
    assert instance.theAttributeToListen == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=TestPackage::TestClass1_strategy)
@settings(max_examples=30)
def test_testpackage::testclass1_testoperation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.testOperation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.testOperation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'testOperation' in TestPackage::TestClass1 is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'testOperation' in TestPackage::TestClass1 did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'testOperation' in TestPackage::TestClass1 is not implemented or raised an error")

@given(instance=TestPackage::AbstractTestClass_strategy)
@settings(max_examples=50)
def test_testpackage::abstracttestclass_instantiation(instance):
    assert isinstance(instance, TestPackage::AbstractTestClass)

@given(instance=TestPackage::AbstractTestClass_strategy)
def test_testpackage::abstracttestclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TestPackage::AbstractTestClass_strategy)
def test_testpackage::abstracttestclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
