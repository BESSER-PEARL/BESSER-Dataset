import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tests_Test,
    tests_TestsModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tests_test_is_not_abstract():
    assert not inspect.isabstract(tests_Test)


def test_tests_test_constructor_exists():
    assert callable(tests_Test.__init__)


def test_tests_test_constructor_args():
    sig = inspect.signature(tests_Test.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_tests_test_has_version():
    assert hasattr(tests_Test, "version")
    descriptor = None
    for klass in tests_Test.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_tests_test_has_id():
    assert hasattr(tests_Test, "id")
    descriptor = None
    for klass in tests_Test.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tests_testsmodel_is_not_abstract():
    assert not inspect.isabstract(tests_TestsModel)


def test_tests_testsmodel_constructor_exists():
    assert callable(tests_TestsModel.__init__)


def test_tests_testsmodel_constructor_args():
    sig = inspect.signature(tests_TestsModel.__init__)
    params = list(sig.parameters.keys())


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
tests_Test_strategy = st.builds(
    tests_Test,
    version=
        safe_text,
    id=
        safe_text
)
tests_TestsModel_strategy = st.builds(
    tests_TestsModel,
)

@given(instance=tests_Test_strategy)
@settings(max_examples=50)
def test_tests_test_instantiation(instance):
    assert isinstance(instance, tests_Test)



@given(instance=tests_Test_strategy)
def test_tests_test_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=tests_Test_strategy)
def test_tests_test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tests_TestsModel_strategy)
@settings(max_examples=50)
def test_tests_testsmodel_instantiation(instance):
    assert isinstance(instance, tests_TestsModel)
