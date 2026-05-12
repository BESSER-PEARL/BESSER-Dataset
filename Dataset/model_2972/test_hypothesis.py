import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    My2_TestClass2,
    TestEnum2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_my2_testclass2_is_not_abstract():
    assert not inspect.isabstract(My2_TestClass2)


def test_my2_testclass2_constructor_exists():
    assert callable(My2_TestClass2.__init__)


def test_my2_testclass2_constructor_args():
    sig = inspect.signature(My2_TestClass2.__init__)
    params = list(sig.parameters.keys())
    assert "testAtt2" in params, "Missing parameter 'testAtt2'"
    assert "testAtt" in params, "Missing parameter 'testAtt'"

def test_my2_testclass2_has_testAtt2():
    assert hasattr(My2_TestClass2, "testAtt2")
    descriptor = None
    for klass in My2_TestClass2.__mro__:
        if "testAtt2" in klass.__dict__:
            descriptor = klass.__dict__["testAtt2"]
            break
    assert isinstance(descriptor, property)

def test_my2_testclass2_has_testAtt():
    assert hasattr(My2_TestClass2, "testAtt")
    descriptor = None
    for klass in My2_TestClass2.__mro__:
        if "testAtt" in klass.__dict__:
            descriptor = klass.__dict__["testAtt"]
            break
    assert isinstance(descriptor, property)

def test_testenum2_exists():
    # Check that the Enumeration exists
    assert TestEnum2 is not None

def test_testenum2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum2]
    expected_literals = [
        "testLiteral2",
        "testLiteral",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum2"


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
My2_TestClass2_strategy = st.builds(
    My2_TestClass2,
    testAtt2=
        safe_text,
    testAtt=
        safe_text
)

@given(instance=My2_TestClass2_strategy)
@settings(max_examples=50)
def test_my2_testclass2_instantiation(instance):
    assert isinstance(instance, My2_TestClass2)



@given(instance=My2_TestClass2_strategy)
def test_my2_testclass2_testAtt2_setter(instance):
    original = instance.testAtt2
    instance.testAtt2 = original
    assert instance.testAtt2 == original



@given(instance=My2_TestClass2_strategy)
def test_my2_testclass2_testAtt_setter(instance):
    original = instance.testAtt
    instance.testAtt = original
    assert instance.testAtt == original
