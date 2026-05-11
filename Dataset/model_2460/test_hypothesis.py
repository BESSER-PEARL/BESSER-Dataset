import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    My::TestClass2,
    My::TestClass,
    TestEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_my::testclass2_is_not_abstract():
    assert not inspect.isabstract(My::TestClass2)


def test_my::testclass2_constructor_exists():
    assert callable(My::TestClass2.__init__)


def test_my::testclass2_constructor_args():
    sig = inspect.signature(My::TestClass2.__init__)
    params = list(sig.parameters.keys())



def test_my::testclass_is_not_abstract():
    assert not inspect.isabstract(My::TestClass)


def test_my::testclass_constructor_exists():
    assert callable(My::TestClass.__init__)


def test_my::testclass_constructor_args():
    sig = inspect.signature(My::TestClass.__init__)
    params = list(sig.parameters.keys())
    assert "testAtt" in params, "Missing parameter 'testAtt'"
    assert "testAtt2" in params, "Missing parameter 'testAtt2'"

def test_my::testclass_has_testAtt():
    assert hasattr(My::TestClass, "testAtt")
    descriptor = None
    for klass in My::TestClass.__mro__:
        if "testAtt" in klass.__dict__:
            descriptor = klass.__dict__["testAtt"]
            break
    assert isinstance(descriptor, property)

def test_my::testclass_has_testAtt2():
    assert hasattr(My::TestClass, "testAtt2")
    descriptor = None
    for klass in My::TestClass.__mro__:
        if "testAtt2" in klass.__dict__:
            descriptor = klass.__dict__["testAtt2"]
            break
    assert isinstance(descriptor, property)

def test_testenum_exists():
    # Check that the Enumeration exists
    assert TestEnum is not None

def test_testenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum]
    expected_literals = [
        "testLiteral",
        "testLiteral2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum"


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
My::TestClass2_strategy = st.builds(
    My::TestClass2,
)
My::TestClass_strategy = st.builds(
    My::TestClass,
    testAtt=
        safe_text,
    testAtt2=
        safe_text
)

@given(instance=My::TestClass2_strategy)
@settings(max_examples=50)
def test_my::testclass2_instantiation(instance):
    assert isinstance(instance, My::TestClass2)

@given(instance=My::TestClass_strategy)
@settings(max_examples=50)
def test_my::testclass_instantiation(instance):
    assert isinstance(instance, My::TestClass)

@given(instance=My::TestClass_strategy)
def test_my::testclass_testAtt_type(instance):
    assert isinstance(instance.testAtt, str)


@given(instance=My::TestClass_strategy)
def test_my::testclass_testAtt_setter(instance):
    original = instance.testAtt
    instance.testAtt = original
    assert instance.testAtt == original

@given(instance=My::TestClass_strategy)
def test_my::testclass_testAtt2_type(instance):
    assert isinstance(instance.testAtt2, str)


@given(instance=My::TestClass_strategy)
def test_my::testclass_testAtt2_setter(instance):
    original = instance.testAtt2
    instance.testAtt2 = original
    assert instance.testAtt2 == original
