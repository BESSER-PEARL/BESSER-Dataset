import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TestElementA,
    testPackage_TestElementB,
    testPackage_Container,
    testPackage_TestElementA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testelementa_is_not_abstract():
    assert not inspect.isabstract(TestElementA)


def test_testelementa_constructor_exists():
    assert callable(TestElementA.__init__)


def test_testelementa_constructor_args():
    sig = inspect.signature(TestElementA.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_testelementb_is_not_abstract():
    assert not inspect.isabstract(testPackage_TestElementB)


def test_testpackage_testelementb_constructor_exists():
    assert callable(testPackage_TestElementB.__init__)


def test_testpackage_testelementb_constructor_args():
    sig = inspect.signature(testPackage_TestElementB.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_container_is_not_abstract():
    assert not inspect.isabstract(testPackage_Container)


def test_testpackage_container_constructor_exists():
    assert callable(testPackage_Container.__init__)


def test_testpackage_container_constructor_args():
    sig = inspect.signature(testPackage_Container.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_testelementa_is_not_abstract():
    assert not inspect.isabstract(testPackage_TestElementA)


def test_testpackage_testelementa_constructor_exists():
    assert callable(testPackage_TestElementA.__init__)


def test_testpackage_testelementa_constructor_args():
    sig = inspect.signature(testPackage_TestElementA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "multi" in params, "Missing parameter 'multi'"

def test_testpackage_testelementa_has_name():
    assert hasattr(testPackage_TestElementA, "name")
    descriptor = None
    for klass in testPackage_TestElementA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testpackage_testelementa_has_multi():
    assert hasattr(testPackage_TestElementA, "multi")
    descriptor = None
    for klass in testPackage_TestElementA.__mro__:
        if "multi" in klass.__dict__:
            descriptor = klass.__dict__["multi"]
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
TestElementA_strategy = st.builds(
    TestElementA,
)
testPackage_TestElementB_strategy = st.builds(
    testPackage_TestElementB,
)
testPackage_Container_strategy = st.builds(
    testPackage_Container,
)
testPackage_TestElementA_strategy = st.builds(
    testPackage_TestElementA,
    name=
        safe_text,
    multi=
        st.integers()
)

@given(instance=TestElementA_strategy)
@settings(max_examples=50)
def test_testelementa_instantiation(instance):
    assert isinstance(instance, TestElementA)

@given(instance=testPackage_TestElementB_strategy)
@settings(max_examples=50)
def test_testpackage_testelementb_instantiation(instance):
    assert isinstance(instance, testPackage_TestElementB)

@given(instance=testPackage_Container_strategy)
@settings(max_examples=50)
def test_testpackage_container_instantiation(instance):
    assert isinstance(instance, testPackage_Container)

@given(instance=testPackage_TestElementA_strategy)
@settings(max_examples=50)
def test_testpackage_testelementa_instantiation(instance):
    assert isinstance(instance, testPackage_TestElementA)



@given(instance=testPackage_TestElementA_strategy)
def test_testpackage_testelementa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=testPackage_TestElementA_strategy)
def test_testpackage_testelementa_multi_setter(instance):
    original = instance.multi
    instance.multi = original
    assert instance.multi == original
