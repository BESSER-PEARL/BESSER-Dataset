import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tests::Test,
    tests::TestsModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tests::test_is_not_abstract():
    assert not inspect.isabstract(tests::Test)


def test_tests::test_constructor_exists():
    assert callable(tests::Test.__init__)


def test_tests::test_constructor_args():
    sig = inspect.signature(tests::Test.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_tests::test_has_version():
    assert hasattr(tests::Test, "version")
    descriptor = None
    for klass in tests::Test.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_tests::test_has_id():
    assert hasattr(tests::Test, "id")
    descriptor = None
    for klass in tests::Test.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tests::testsmodel_is_not_abstract():
    assert not inspect.isabstract(tests::TestsModel)


def test_tests::testsmodel_constructor_exists():
    assert callable(tests::TestsModel.__init__)


def test_tests::testsmodel_constructor_args():
    sig = inspect.signature(tests::TestsModel.__init__)
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
tests::Test_strategy = st.builds(
    tests::Test,
    version=
        safe_text,
    id=
        safe_text
)
tests::TestsModel_strategy = st.builds(
    tests::TestsModel,
)

@given(instance=tests::Test_strategy)
@settings(max_examples=50)
def test_tests::test_instantiation(instance):
    assert isinstance(instance, tests::Test)

@given(instance=tests::Test_strategy)
def test_tests::test_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=tests::Test_strategy)
def test_tests::test_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=tests::Test_strategy)
def test_tests::test_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=tests::Test_strategy)
def test_tests::test_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tests::TestsModel_strategy)
@settings(max_examples=50)
def test_tests::testsmodel_instantiation(instance):
    assert isinstance(instance, tests::TestsModel)
