import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TestElementA,
    testPackage::TestElementB,
    testPackage::Container,
    testPackage::TestElementA,
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



def test_testpackage::testelementb_is_not_abstract():
    assert not inspect.isabstract(testPackage::TestElementB)


def test_testpackage::testelementb_constructor_exists():
    assert callable(testPackage::TestElementB.__init__)


def test_testpackage::testelementb_constructor_args():
    sig = inspect.signature(testPackage::TestElementB.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::container_is_not_abstract():
    assert not inspect.isabstract(testPackage::Container)


def test_testpackage::container_constructor_exists():
    assert callable(testPackage::Container.__init__)


def test_testpackage::container_constructor_args():
    sig = inspect.signature(testPackage::Container.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::testelementa_is_not_abstract():
    assert not inspect.isabstract(testPackage::TestElementA)


def test_testpackage::testelementa_constructor_exists():
    assert callable(testPackage::TestElementA.__init__)


def test_testpackage::testelementa_constructor_args():
    sig = inspect.signature(testPackage::TestElementA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "multi" in params, "Missing parameter 'multi'"

def test_testpackage::testelementa_has_name():
    assert hasattr(testPackage::TestElementA, "name")
    descriptor = None
    for klass in testPackage::TestElementA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testpackage::testelementa_has_multi():
    assert hasattr(testPackage::TestElementA, "multi")
    descriptor = None
    for klass in testPackage::TestElementA.__mro__:
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
testPackage::TestElementB_strategy = st.builds(
    testPackage::TestElementB,
)
testPackage::Container_strategy = st.builds(
    testPackage::Container,
)
testPackage::TestElementA_strategy = st.builds(
    testPackage::TestElementA,
    name=
        safe_text,
    multi=
        st.integers()
)

@given(instance=TestElementA_strategy)
@settings(max_examples=50)
def test_testelementa_instantiation(instance):
    assert isinstance(instance, TestElementA)

@given(instance=testPackage::TestElementB_strategy)
@settings(max_examples=50)
def test_testpackage::testelementb_instantiation(instance):
    assert isinstance(instance, testPackage::TestElementB)

@given(instance=testPackage::Container_strategy)
@settings(max_examples=50)
def test_testpackage::container_instantiation(instance):
    assert isinstance(instance, testPackage::Container)

@given(instance=testPackage::TestElementA_strategy)
@settings(max_examples=50)
def test_testpackage::testelementa_instantiation(instance):
    assert isinstance(instance, testPackage::TestElementA)

@given(instance=testPackage::TestElementA_strategy)
def test_testpackage::testelementa_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testPackage::TestElementA_strategy)
def test_testpackage::testelementa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testPackage::TestElementA_strategy)
def test_testpackage::testelementa_multi_type(instance):
    assert isinstance(instance.multi, int)


@given(instance=testPackage::TestElementA_strategy)
def test_testpackage::testelementa_multi_setter(instance):
    original = instance.multi
    instance.multi = original
    assert instance.multi == original
